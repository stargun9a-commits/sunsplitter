#!/bin/bash
# 🧠 VOID-DRONE: ENVIRONMENT ACTIVATOR
# Auto-activates the local forensic toolchain upon directory entry.

CONDA_ENV="void-drone"

# 1. Activate the Conda environment if not already active
if [[ "$CONDA_DEFAULT_ENV" != "$CONDA_ENV" ]]; then
    echo ">>> Activating forensic environment: $CONDA_ENV"
    # Check if conda is available
    if command -v conda &> /dev/null; then
        eval "$(conda shell.bash hook)"
        conda activate "$CONDA_ENV" || echo "WARNING: Conda environment '$CONDA_ENV' not found. Run 'conda create -n $CONDA_ENV python=3.11' first."
    else
        echo "ERROR: Conda not found. Please install Miniconda to manage the AI toolchain."
    fi
fi

# 2. Export local source to PATH for easy execution
export PATH="$PWD/src:$PATH"

# 3. Export forensic environment variables
export PROJECT_ROOT="$PWD"
export BLUEPRINTS="$PWD/blueprints"
export ISO_DATA="$PWD/data"

echo "✅ Environment Ready: Void-Drone Substrate."
