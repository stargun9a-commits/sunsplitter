#!/bin/bash
# 🛸 PROJECT GHOST-MATRIX: KAGGLE BOOTSTRAP
# Installs VS Code CLI and initializes the Remote Tunnel

echo ">>> Initializing Remote Tunnel Bootstrap..."
curl -Lk 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-x64' --output vscode_cli.tar.gz
tar -xf vscode_cli.tar.gz -C /usr/local/bin
rm vscode_cli.tar.gz

echo ">>> Starting VS Code Tunnel. Authenticate via github.com/login/device"
# The --accept-server-license-terms flag automates the prompt
code tunnel --accept-server-license-terms
