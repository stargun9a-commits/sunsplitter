# 🛸 Space-Drill: The Execution Orchestrator

Welcome to the **Space-Drill** workflow. This directory houses the primary builder engine for your AI.

## 🎯 Purpose
While `nova-reactor` is used for auditing and sanity checking, `space-drill` is used to get things built. This engine is designed to execute deterministic codebase modifications, orchestrate multi-step engineering tasks, and conduct Deep Research via cognitive forcing functions.

## 📂 Structure
*   **`system-prompt.md`**: The brain of Space-Drill. Point your AI here to initialize the execution and orchestration persona.
*   **`modules/deep-research.md`**: The synthesis module. It forces the agent to use anti-hallucination protocols (Chain of Verification & Chain of Density) when you need to research a new topic.
*   **`modules/engineering-execution.md`**: The build module. It enforces the SAMF-E deployment contracts and the Graph of Verification (GoV) for complex scripting.
*   **`memory/NOTES.md`**: The isolated memory bank. Used to prevent context window bloat during long-horizon engineering sessions.

## 🛠️ How to Use
Start a new agent session and run:
> *"I have a new task regarding [Task Description]. Please ingest `_g-agent/space-drill/system-prompt.md` and initialize the orchestrator to determine the best execution route."*
