# 🧲 TOOL: CORE-SCANNER (COGNITIVE LOAD GAUGE)
## Classification: Global Context Optimization

### **1. Purpose: The Saturation Check**
The `core-scanner` tool evaluates the physical byte-size of the underlying Antigravity brain log to approximate how much of the immediate context window has been consumed. This provides a mathematical trigger for when the user should execute the `snapshot` tool before the system begins aggressively truncating (forgetting) early operational directives.

### **2. Execution Protocol**
When a user invokes `core-scanner`, the agent must execute the following via terminal:

1. Identify the current session's `Conversation ID` from the system metadata.
2. Execute the python script: `python3 _g-agent/single-core/scanner.py <Conversation_ID>`
3. Return the terminal output directly to the user.

### **3. Actionable Triggers**
- **0% - 50%**: Stable. Continue operations normally.
- **50% - 85%**: Warning. The agent will begin leaning heavily on its static `.md` files as immediate conversation memory begins to cycle out.
- **85%+ (Critical)**: Imminent Truncation. The agent MUST advise the user to immediately run the `snapshot` tool to generate an `ACTIVE_STATE.md` file before migrating to a fresh conversation.
