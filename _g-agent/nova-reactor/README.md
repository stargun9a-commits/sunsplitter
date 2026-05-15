# ☢️ Nova-Reactor: The Adversarial Sanity Checker

Welcome to the **Nova-Reactor** workflow. This directory houses the "Red Team" prompt engine designed specifically for analytical validation.

## 🎯 Purpose
When Gemini Deep Research (or any LLM) generates a massive architectural blueprint, it is prone to **Reality Gaps**. It might hallucinate that you can run a 70B parameter model locally without sufficient VRAM, or it might propose an API route that ignores authentication limits.

Nova-Reactor is designed to ingest those reports and aggressively interrogate them. It does not write code; it validates feasibility.

## 📂 Structure
*   **`system-prompt.md`**: The brain of Nova-Reactor. Point your AI here to initialize the sanity-checking persona.
*   **`modules/feasibility-audit.md`**: The core interrogation matrix. It forces the AI to check hardware constraints, OPSEC degradation, and API logic.
*   **`memory/NOTES.md`**: The isolated memory bank. Used to log confirmed Reality Gaps and verified architectures without bleeding into your execution environments.

## 🛠️ How to Use
Start a new agent session (or clear your current context) and run:
> *"Please ingest the Deep Research report at `[Path to Report]`. Then, load your instructions from `_g-agent/nova-reactor/system-prompt.md` and execute a Feasibility Audit to find any Reality Gaps."*
