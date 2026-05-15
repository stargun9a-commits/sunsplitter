# 🚀 _g-agent: Compound Multi-Agent Orchestrator (V3)

Welcome to the `_g-agent` root! This directory houses a highly optimized, modular prompt engine designed to elevate an AI coding assistant from a basic autocomplete utility into a rigorous, autonomous system architect.

## 📂 Architecture Overview

This engine utilizes a multi-workflow topology, splitting responsibilities between execution and analytical validation:

### 1. `space-drill/` (Execution & Orchestration)
This is the core engineering engine. It builds the simulations and plans the architectures.
*   **`system-prompt.md`**: The brain. Contains core routing logic and security defenses.
*   **`modules/deep-research.md`**: The synthesis module (Chain of Verification & Chain of Density).
*   **`modules/engineering-execution.md`**: The build module (SAMF-E contracts & GoV).
*   **`memory/NOTES.md`**: The execution memory bank for context pruning.

### 2. `nova-reactor/` (Validation & Sanity Check)
This is the adversarial "Red Team" engine. It interrogates research reports to ensure they are actually buildable in reality.
*   **`system-prompt.md`**: The core objective to hunt for technical hallucinations.
*   **`modules/feasibility-audit.md`**: The "Reality Gap" interrogation matrix (validating hardware, OPSEC, and API limits).
*   **`modules/narrative-synthesis.md`**: Translates technical reports into documentary scripts/podcast narration for story-checking.
*   **`modules/futurist-extrapolation.md`**: Predicts future evolutions of the attack vector on next-gen AI stacks.
*   **`memory/NOTES.md`**: Isolated memory to prevent execution context bleed.

### 3. `council/` (Shared Agent Personas)
This is a shared resource for both workflows, powered by the MCP. It acts as a strict Phase-Gate reviewer.
*   `space-drill` uses the Council to review complex scripts before execution (Phase 2).
*   `nova-reactor` uses the Council to stress-test architectures during feasibility audits (Phase 1).

### 4. `skills/` (Shared Expertise)
This directory houses reusable, stateless instructional files (e.g., Karpathy guidelines, dark-factory principles). Both workflows can ingest these files to dynamically load specific coding styles or operational paradigms on demand.

### 5. `specs/` (Hardware & Standardization Truth Layer)
This directory contains the immutable constraints of the physical host machine, the virtual machines, and the required file-naming standards. Both orchestrators are hardwired to ingest these specs before generating any logic to prevent hardware bottlenecks and formatting drift.

### 6. `single-core/` (Contextual Tooling & Plugins)
This directory houses standalone, stateless utility scripts designed to manage the agent's active memory and cognitive load.
*   **`snapshot.md`**: The Context Optimizer. Collapses sprawling research into an `ACTIVE_STATE.md` file for seamless migration to fresh conversations.
*   **`core-scanner.md` / `scanner.py`**: The Cognitive Load Gauge. Physically measures the underlying Antigravity `.system_generated` logs to return a mathematical "Saturation %", alerting the user when a snapshot is required.

### 7. Temporal Grounding (Crucial Reality Layer)
**MANDATORY**: You are operating in **May 2026**. All forensic analysis, narrative scripting, and technical extrapolation must be grounded in this actual current date. Do not hallucinate historical context or relative timelines; cross-reference the `current_date` metadata in every session.

---

## 🛠️ Optimal Prompt Engineering: How to Use

To get the absolute best performance out of your AI agent (whether in Antigravity, Gemini CLI, or Claude Code), follow these operational guidelines:

### 1. Initialize the Execution Orchestrator
When you start a new complex task and need to build something, point the agent to the **space-drill** orchestrator:
> *"I have a new task regarding [Task Description]. Please ingest `_g-agent/space-drill/system-prompt.md` and initialize the orchestrator to determine the best execution route."*

### 2. Triggering "Deep Research" (Zero-Hallucination)
When you need a feasibility study or project plan, invoke Deep Research inside space-drill:
> *"We need to design a new data pipeline. Please route to the Deep Research module. Execute a Factored Chain of Verification (CoVe) on your plan before writing any code."*

### 3. Enforcing "Agentic Memory" & Context Pruning
Over time, the agent's context window fills up with old `grep` searches. You must actively manage this by utilizing the workflow's specific memory bank:
> *"You just pulled a massive directory tree. Please synthesize the critical findings into `_g-agent/space-drill/memory/NOTES.md`, and then actively prune the raw tool output from your active context window so we can maintain focus."*

### 4. Running a Reality Check (Nova-Reactor)
When you receive a massive AI-generated research report and want to ensure it isn't hallucinating impossible hardware or OPSEC failures, point a *new* agent session at the **nova-reactor** workflow:
> *"Please ingest the report at `[Path to Report]`. Then, load your instructions from `_g-agent/nova-reactor/system-prompt.md` and execute a Feasibility Audit to find any Reality Gaps."*

### 5. Managing Cognitive Load (Single-Core Tools)
When the session is dragging or you want to snapshot your progress before migrating to a clean window, utilize the standalone context plugins:
> *"Run the `core-scanner` tool to check my cognitive saturation."*
> *"Execute the `snapshot` tool to compress our state for migration."*

---

## 📦 Portability

This engine is designed to be fully portable. If you start a new project, simply copy the entire `_g-agent` directory into the root of the new workspace. The agent will instantly understand the routing logic and memory structures.
