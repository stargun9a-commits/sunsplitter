#!/bin/bash
# ===================================================================
# AGENT COUNCIL: MCP CONFIGURATION SCRIPT
# ===================================================================
# This script ensures the ai-agent-council-mcp is registered in the 
# host's mcp_config.json, making the Agent Council portable across 
# different IDEs and workspaces.

CONFIG_PATH="$HOME/.gemini/antigravity/mcp_config.json"

echo "Checking for MCP configuration at $CONFIG_PATH..."

if [ ! -f "$CONFIG_PATH" ]; then
    echo "Creating new mcp_config.json..."
    echo '{"mcpServers": {}}' > "$CONFIG_PATH"
fi

# Check if the council is already installed
if grep -q "ai-agent-council-mcp" "$CONFIG_PATH"; then
    echo "✅ Agent Council MCP is already configured."
    exit 0
fi

echo "Adding Agent Council MCP to configuration..."

# Inject the server configuration using a temporary file
cat << 'EOF' > /tmp/mcp_patch.json
{
  "mcpServers": {
    "agent-council": {
      "command": "npx",
      "args": ["-y", "ai-agent-council-mcp"]
    }
  }
}
EOF

# In a real environment, you'd use jq to merge, but we'll append a manual merge for simplicity
# if jq is available.
if command -v jq >/dev/null 2>&1; then
    jq -s '.[0] * .[1]' "$CONFIG_PATH" /tmp/mcp_patch.json > /tmp/mcp_merged.json
    mv /tmp/mcp_merged.json "$CONFIG_PATH"
    echo "✅ Agent Council MCP successfully added via jq."
else
    echo "⚠️ 'jq' not found. Please manually add the following to $CONFIG_PATH:"
    cat /tmp/mcp_patch.json
fi

rm -f /tmp/mcp_patch.json
echo "Restart your IDE/Agent to load the new MCP tools."
