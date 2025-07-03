# Python Project Stats Viewer

A lightweight Python script that analyzes Python projects to provide detailed statistics about code structure, including line counts, function definitions, and class declarations.

## Features

- **Recursive directory scanning** - Analyzes all Python files in a directory tree
- **AST-based analysis** - Uses Python's Abstract Syntax Tree for accurate function and class counting
- **Smart directory filtering** - Automatically ignores common non-source directories (venv, .git, __pycache__, etc.)
- **Custom ignore patterns** - Add your own directories to exclude from analysis
- **Detailed breakdown** - Shows statistics for each file and project-wide summaries
- **Error handling** - Gracefully handles files that can't be parsed

## Usage

1. Run the script:
   ```bash
   python code_analyzer.py
   ```

2. Enter the directory path you want to analyze when prompted

3. Optionally add additional directories to ignore (press Enter twice when done)

4. View the detailed analysis results

## Example Output

```
Ignored directories:
.env, .git, .idea, .mypy_cache, .pytest_cache, .venv, .vscode, __pycache__, build, dist, env, node_modules, venv

Breakdown by file:
src/main.py:
  Lines: 156
  Functions: 12
  Classes: 3
src/utils/helpers.py:
  Lines: 89
  Functions: 8
  Classes: 1

Summary:
Total Python files: 15
Total lines of code: 2,347
Total functions: 87
Total classes: 12
Average lines per file: 156.5
Average functions per file: 5.8
Average classes per file: 0.8
```

## Default Ignored Directories

The following directories are automatically excluded from analysis:
- `.git`, `.conda`, `venv`, `.venv`, `env`, `.env`
- `__pycache__`, `.pytest_cache`, `.mypy_cache`
- `node_modules`, `build`, `dist`
- `.idea`, `.vscode`

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## How It Works

The script uses Python's `ast` module to parse each Python file and count:
- Function definitions (including async functions)
- Class definitions
- Total lines of code

This AST-based approach ensures accurate counting even with complex code structures, nested definitions, and various coding styles.

---

**Disclaimer:** This code was written by a Large Language Model (LLM).
