# ZeroNit local benchmark arena

Synthetic Python + TypeScript service changes with executable behavior contracts.
No network, package installation, GitHub App or background service is needed for local runtimes.
Requirements: Python3.11+ and Node24+ (native TypeScript type stripping).

Run `python checks/runtime.py all` on main or a patched branch. Broken branches intentionally fail
one behavior contract. The scanner is a separately installed ZeroNit CLI; see PUSH_AND_SHOOTOUT_GUIDE.md.

The four defects exercise shared-state lost updates, a missing action authorization gate,
pool exhaustion after a real SQLite query error, and real SQLite SQL injection.
The action uses in-memory auth/ORM doubles to model a Next-style Server Action. This is not a
deployed Next.js integration test. The pool has one actual SQLite connection and bounded capacity.
SQL payloads run only against in-memory synthetic data.

Main is clean. Each `pr-0x-*` branch is based on main; its `-patched` child repairs that change.
The clean-control pair has zero expected findings in both states; it does not introduce a fake outage.

This is a transparent demonstration, not a blinded or representative benchmark. Defect families
are deliberately selected from ZeroNit's catalog; branch labels and tests reveal those families.
Compare both products on identical pinned revisions, retain all output, and adjudicate every finding.
Absence of a scanner finding is not proof of general correctness. Runtime oracles remain outside
the analyzer; the analyzer receives ordinary repository files and Git changes.

Provenance: adapted from Shinra's requested arena structure and existing factory fixture patterns.
The runnable service doubles, controls and branch construction are new work for this arena.
License: MIT.
