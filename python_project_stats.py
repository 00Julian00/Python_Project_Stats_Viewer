import os
import ast

DEFAULT_IGNORE_DIRS = {
    '.git', '.conda', 'venv', '.venv', 'env', '.env',
    '__pycache__', '.pytest_cache', '.mypy_cache',
    'node_modules', 'build', 'dist', '.idea', '.vscode'
}

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.functions = 0
        self.classes = 0
    
    def visit_FunctionDef(self, node):
        self.functions += 1
        self.generic_visit(node)
        
    def visit_AsyncFunctionDef(self, node):
        self.functions += 1
        self.generic_visit(node)
    
    def visit_ClassDef(self, node):
        self.classes += 1
        self.generic_visit(node)

def analyze_file(file_content):
    try:
        tree = ast.parse(file_content)
        analyzer = CodeAnalyzer()
        analyzer.visit(tree)
        return analyzer.functions, analyzer.classes
    except SyntaxError:
        return 0, 0

def count_lines_in_py_files(directory, ignore_dirs=None):
    """
    Recursively search through a directory and analyze Python files
    
    Returns:
        tuple: (total_lines, total_files, total_functions, total_classes, 
                dict of file info including lines, functions, and classes)
    """
    total_lines = total_functions = total_classes = total_files = 0
    file_info = {}
    
    dirs_to_ignore = DEFAULT_IGNORE_DIRS.copy()
    if ignore_dirs:
        dirs_to_ignore.update(ignore_dirs)
    
    base_dir = os.path.abspath(directory)
    
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in dirs_to_ignore]
        py_files = [f for f in files if f.endswith('.py')]
        
        for py_file in py_files:
            abs_path = os.path.join(root, py_file)
            rel_path = os.path.relpath(abs_path, base_dir)
            
            try:
                with open(abs_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = len(content.splitlines())
                    funcs, classes = analyze_file(content)
                    
                    total_lines += lines
                    total_functions += funcs
                    total_classes += classes
                    total_files += 1
                    
                    file_info[rel_path] = {
                        'lines': lines,
                        'functions': funcs,
                        'classes': classes
                    }
            except Exception as e:
                print(f"Error reading file {rel_path}: {e}")
    
    return total_lines, total_files, total_functions, total_classes, file_info

def main():
    directory = input("Enter the directory path to analyze: ")
    
    if not os.path.isdir(directory):
        print("Error: Invalid directory path")
        return
    
    print("\nEnter additional directories to ignore (one per line)")
    print("Press Enter twice when done:")
    
    custom_ignore = set()
    while True:
        dir_name = input().strip()
        if not dir_name:
            break
        custom_ignore.add(dir_name)
    
    print("\nIgnored directories:")
    all_ignored = DEFAULT_IGNORE_DIRS.union(custom_ignore)
    print(", ".join(sorted(all_ignored)))
    
    total_lines, total_files, total_functions, total_classes, file_info = count_lines_in_py_files(directory, custom_ignore)
    
    print("\nBreakdown by file:")
    for file_path, info in sorted(file_info.items()):
        print(f"{file_path}:")
        print(f"  Lines: {info['lines']}")
        print(f"  Functions: {info['functions']}")
        print(f"  Classes: {info['classes']}")
    
    print(f"\nSummary:")
    print(f"Total Python files: {total_files}")
    print(f"Total lines of code: {total_lines}")
    print(f"Total functions: {total_functions}")
    print(f"Total classes: {total_classes}")
    print(f"Average lines per file: {total_lines / total_files:.1f}")
    print(f"Average functions per file: {total_functions / total_files:.1f}")
    print(f"Average classes per file: {total_classes / total_files:.1f}")

if __name__ == "__main__":
    main()