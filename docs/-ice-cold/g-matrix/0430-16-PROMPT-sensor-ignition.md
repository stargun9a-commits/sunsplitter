# MISSION: SKY-CRANE (V16) - SENSOR IGNITION
## Objective: Deterministic Build Logic for BGP Forensic Sensors
## Date: 04-28-2026

### 🛠️ SITUATION REPORT
The Debian 12 "Primal" substrate is operational. Python 3.12 is anchored via the `._pth` kill-switch at `/opt/SovereignHub/bin/`. We now require the "Sensors": `wandio` and `libbgpstream`.

**The Architectural Challenge:**
1. **glibc 2.39 Compatibility**: Debian 12 uses a modern glibc where `pthread_yield` is deprecated. Compilation of `libbgpstream` and `wandio` will fail unless patched with `sched_yield`.
2. **Pillar II (ABI Determinism)**: All libraries (`.so` files) MUST be compiled with `$ORIGIN` RPATHs. They must link to each other within `/opt/SovereignHub/lib` and NEVER search the guest's `/usr/lib/` or the host's paths.

### 🧬 [SAMF-E] RESEARCH OBJECTIVES
1. **[E_1] THE GLIBC WIRE-IN**:
    - Provide the exact `sed` or `patch` directives to replace `pthread_yield` with `sched_yield` in the `libbgpstream` and `wandio` source trees.
    - Reference: Header `<sched.h>` is required for the shim.
2. **[E_2] DETERMINISTIC LINKAGE**:
    - Architect the `configure` and `make` flags (specifically `LDFLAGS` and `CPPFLAGS`) to force:
        - `DT_RPATH` injection using `\$ORIGIN/../lib`.
        - Static linking of non-essential dependencies where possible.
        - Installation prefix set strictly to `/opt/SovereignHub`.
3. **[E_3] PYTHON BINDINGS (PYBGPSTREAM)**:
    - Detail the `pip install` or `setup.py` environment variables required to build the `pybgpstream` C-extension against the Sovereign Hub's local `include` and `lib` directories.
    - Ensure the extension is "Path-Blind" and does not trigger upward landmark traversal.

### 📦 ATTACHMENT INSTRUCTIONS (FOR HUMAN OPERATOR)
Please attach the following documents to the Gemini Deep Research interface:
1. `g-matrix/docs/0428-bible-lessons.md` (Forensic Bible V11)
2. `g-matrix/src/0428-GLIBC-WIRE-IN.md` (Initial glibc patch notes)

**MISSION CRITICAL**: Use the "Physical Lie" architecture. The guest OS must remain a transparent container. All forensic intelligence must reside within the Sovereign Hub.
