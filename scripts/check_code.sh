#!/bin/bash

set -e

# Check if a file or directory is passed as an argument
if [ "$#" -eq 0 ]; then
  TARGETS="./"  # Default to the current directory if no arguments are provided
else
  TARGETS="$@"  # Use the arguments passed to the script
fi

echo "Running Black for code formatting..."
black $TARGETS

echo "Running ruff for linting..."
ruff check $TARGETS

echo "Generating requirements.txt from installed packages..."
pip list --format=freeze > requirements.txt

echo "Pipeline script was executed successfully"
