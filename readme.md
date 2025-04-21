# Python Virtual Environment Setup Guide

This guide explains how to set up a Python virtual environment and install dependencies on Windows, macOS, and Linux operating systems.

## What is a Virtual Environment?

A virtual environment is an isolated Python environment that allows you to install packages for a specific project without affecting your system's global Python installation. This helps avoid dependency conflicts between different projects.

## Prerequisites

- Python 3.6 or higher installed on your system
- Basic knowledge of command-line operations

## Setup Instructions

### Windows

#### Creating a Virtual Environment

1. Open Command Prompt or PowerShell
2. Navigate to your project directory:
   ```
   cd path\to\your\project
   ```
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   ```
   venv\Scripts\activate
   ```
   You should now see `(venv)` at the beginning of your command prompt line.

#### Installing Dependencies

With the virtual environment activated, install dependencies:
```
pip install -r requirements.txt
```

#### Deactivating the Virtual Environment

When you're done working, deactivate the environment:
```
deactivate
```

### macOS / Linux

#### Creating a Virtual Environment

1. Open Terminal
2. Navigate to your project directory:
   ```
   cd path/to/your/project
   ```
3. Create a virtual environment:
   ```
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```
   You should now see `(venv)` at the beginning of your terminal line.

#### Installing Dependencies

With the virtual environment activated, install dependencies:
```
pip install -r requirements.txt
```

#### Deactivating the Virtual Environment

When you're done working, deactivate the environment:
```
deactivate
```

On some Linux/macOS systems, you might need to use `python3` instead of `python`:
```
python3 -m venv venv
```

### Permission Denied

If you encounter permission errors on Linux/macOS:
```
chmod +x venv/bin/activate
```
Then try activating again.

### 'venv' is not recognized (Windows)

Make sure you have the latest Python version installed and added to your PATH. You can also try:
```
py -m venv venv
```

### pip command not found

If pip is not found after activating the virtual environment:
```
python -m pip install --upgrade pip
```

## Example Workflow

```
# Create project directory
mkdir my_project
cd my_project

# Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install packages
pip install pandas numpy matplotlib

# Save dependencies
pip freeze > requirements.txt

# Later, to restore the environment elsewhere
# (after creating and activating a new venv)
pip install -r requirements.txt
```
