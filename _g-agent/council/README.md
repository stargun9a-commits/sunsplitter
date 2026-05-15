# Agent Council - GHOST-MATRIX Operations Guide

## Overview
The **Agent Council** is an MCP (Model Context Protocol) integration designed to prevent "Yes-Man" AI behavior and enforce rigorous architectural stress-testing. By convening a panel of specialized, simulated experts, we can debate implementations, surface edge cases, and validate security before any code is deployed to the Sovereign Hub.

## Workflow Integration: The Phase-Gate Model
Do not invoke the council for trivial syntax errors or basic refactoring. The council acts as a strict **Gatekeeper** at two critical phases:

1.  **Phase 1: Architectural Planning**
    *   **Trigger:** When a new system design or deployment strategy (e.g., Network Isolation Bypass) is drafted.
    *   **Action:** The council debates the viability of the approach against our constraints (Zero-Drag, Deterministic, Air-gapped).
2.  **Phase 2: Code & Deployment Review**
    *   **Trigger:** Before executing complex shell scripts (e.g., `genesis-v2.sh`) or C-level compilations.
    *   **Action:** The council reviews for race conditions, glibc deadlocks, ABI sealing flaws, and silent failures.

## Standard Operating Personas
When invoking the council, specify the required personas based on the task context. 

### 🛡️ The Paranoid SecOps Lead
*   **Focus:** Complete isolation, forensic integrity, and zero-trust boundaries.
*   **Duties:** Aggressively hunts for potential data leaks, improper permissions, broken air-gaps, and supply-chain vulnerabilities in dependencies.

### ⚙️ The C/Systems Architect
*   **Focus:** Kernel-level interactions, memory safety, and POSIX compliance.
*   **Duties:** Scrutinizes build flags, dynamic linker behavior (`$ORIGIN`), threading models (glibc deadlocks), and Virtio-FS bridge performance optimizations.

### 📡 The BGP Forensic Analyst
*   **Focus:** Data fidelity, routing anomaly accuracy, and network topology mapping.
*   **Duties:** Validates the logic behind anomaly detection algorithms (MAD-scores, threshold tuning), ensures realistic baseline windows, and prevents false-positive cascades.

## How to Request a Review
To initiate a council session, use the provided `REVIEW_TEMPLATE.md`. Pass the filled template to Antigravity and explicitly state: 
> *"Please convene the Agent Council to review this proposal using the provided template."*
