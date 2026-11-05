# Development Roadmap

## Approach

Build V1.0 in small, verifiable increments. Keep the working V0.1 CLI
available until equivalent GUI workflows are tested. Avoid a rewrite
that removes known-good behaviour prematurely.

## Phase 0 --- Baseline and repository preparation

-   Confirm remote and latest commit.
-   Confirm working tree.
-   Tag or identify verified V0.1 baseline.
-   Review source tree and dependencies.
-   Check `.gitignore` for virtual environments, secrets, local logs and
    user sessions.
-   Add blueprint under `docs/blueprint/`.
-   Record known issues and open questions.

**Exit:** Restorable baseline, understood project structure and
documented manual workflows.

## Phase 1 --- Code review and stabilisation

-   Review diagnostic, repair, session and report modules.
-   Identify unclear boundaries and duplication.
-   Add/improve unit tests.
-   Validate session schema and error handling.
-   Review Windows Update cache cleanup.
-   Improve UNKNOWN explanations for drive and battery data.

**Exit:** Regression tests cover existing features; failures are
structured; risk and verification behaviour are documented.

## Phase 2 --- Architecture and UI prototype

-   Build a small PySide6 prototype.
-   Create main window/navigation shell.
-   Add placeholder dashboard, diagnostics and reports pages.
-   Demonstrate background work and progress.
-   Connect one read-only diagnostic through an application service.
-   Test on target Windows.

**Exit:** UI stays responsive; OS logic is outside UI; results display
accurately.

## Phase 3 --- Core desktop workflows

-   Dashboard and recent scan summary.
-   Full and individual diagnostics.
-   Results with explanations and technical detail.
-   Session history and details.
-   Settings and mode selection.
-   Structured logs and error presentation.

**Exit:** GUI runs existing diagnostics; sessions save/reopen; modes
have defined differences.

## Phase 4 --- Repair Centre

-   Repair catalogue and categories.
-   Preview and risk display.
-   Confirmation dialogs.
-   Permission handling.
-   Progress, safe cancellation and results.
-   Repair history.
-   Test in disposable VMs.

**Exit:** All actions follow safety lifecycle; partial success, failure
and cancellation are distinguishable; unverified repairs are not
reported as successful.

## Phase 5 --- Expanded diagnostics and reports

Candidate features: improved drive/battery data, GPU/motherboard
information, network diagnostics, Windows integrity checks, PDF/JSON
export, technician notes and device labels. Prioritise reliability and
value over menu count.

## Phase 6 --- Packaging and installation

-   Select packaging tool.
-   Build from clean environment.
-   Test in clean Windows VM without Python.
-   Create installer and desktop shortcut.
-   Verify data paths and permissions.
-   Test upgrade, uninstall and reinstall.
-   Decide user-data retention on uninstall.
-   Evaluate code signing.

**Exit:** Installer works on supported configurations and app runs
outside the developer environment.

## Phase 7 --- Commercial readiness

-   Document Windows support.
-   Prepare user documentation.
-   Define licence and activation approach.
-   Establish update/release process.
-   Complete privacy/security review.
-   Test with all three audiences.
-   Create feedback/support process.

**Exit:** Critical defects resolved, legal/privacy information clear,
release artefacts tested, support/update responsibilities defined.

## Suggested version milestones

-   V0.1 --- Existing CLI prototype and verified baseline.
-   V0.2 --- Stabilised engine, tests and clearer contracts.
-   V0.3 --- Desktop UI prototype with read-only diagnostics.
-   V0.5 --- Core desktop workflows and session history.
-   V0.8 --- Repair Centre and expanded reporting under broader testing.
-   V1.0 --- First release meeting agreed functional, safety,
    installation and documentation criteria.

These are planning milestones, not deadlines.
