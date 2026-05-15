# 🏛️ Agent Council Review Request

**Date:** [YYYY-MM-DD]
**Component:** [e.g., genesis-v2.sh, matrix-discovery-v2.py, Memory Backing Config]
**Phase:** [Architectural Planning | Code Review]

---

## 1. Context & Objective
*Provide a brief summary of what this component/plan is supposed to do and why it is necessary.*

> **Example:** This script automates the deployment of the isolated Debian 12 VM and establishes the Virtio-FS bridge for the Sovereign Hub.

## 2. Requested Personas
*Select the experts required for this specific review. (Uncomment those needed)*

- [ ] 🛡️ **The Paranoid SecOps Lead** (Review for leaks, air-gap integrity, and permissions)
- [ ] ⚙️ **The C/Systems Architect** (Review for POSIX compliance, deadlocks, and kernel interactions)
- [ ] 📡 **The BGP Forensic Analyst** (Review for detection logic, data fidelity, and routing nuances)
- [ ] 🛠️ **Other (Specify):** [e.g., Python Build Specialist]

## 3. Mission Constraints
*List the hard rules the council must enforce when reviewing this artifact.*

1. **[E_3] Zero-Drag:** Must minimize dependencies and overhead.
2. **[E_4] Deterministic:** Must be fully reproducible without external internet access during runtime.
3. **[Constraint 3]:** [Any component-specific constraints, e.g., "Must seal ABI to $ORIGIN"]

## 4. Specific Concerns / Questions for the Council
*Direct the council's attention to areas of uncertainty.*

1. *Are there any race conditions in the systemd service injection?*
2. *Will this specific linker flag break under glibc 2.39?*

---

## 5. The Artifact
*Paste the code, script, or architectural design document below for the council to analyze.*

```[language]
[Paste content here]
```
