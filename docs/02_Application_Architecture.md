# Application Architecture

## Direction

Evolve the Python V0.1 application into a layered desktop application.
The GUI must not contain diagnostic or repair logic. It calls
application services, which coordinate domain logic and operating-system
integrations.

``` text
Presentation: PySide6 windows, pages, widgets, dialogs
                         |
Application: use cases, scan/repair orchestration, preferences
                         |
Domain: diagnostics, findings, repair actions, risk, sessions
                         |
Infrastructure: Windows APIs, filesystem, processes, persistence,
                logging, report export
```

## Technology candidates

  Concern           Proposal                          Status
  ----------------- --------------------------------- --------------------------------------
  Language          Python                            Existing
  Desktop UI        PySide6                           Preferred candidate; prototype first
  Packaging         PyInstaller or equivalent         Evaluate
  Installer         Windows installer technology      Select later
  Local data        JSON initially; evaluate SQLite   Open decision
  Tests             pytest                            Existing
  Version control   Git/private GitHub                Existing
  Reports           PDF and JSON                      Proposed

Review dependency maintenance and licences before adopting packages.

## Proposed structure

``` text
PC-Repair-Toolkit/
├── app/
│   ├── main.py
│   ├── bootstrap.py
│   ├── domain/
│   │   ├── diagnostics/
│   │   ├── repairs/
│   │   ├── sessions/
│   │   └── models/
│   ├── application/
│   │   ├── services/
│   │   ├── use_cases/
│   │   └── orchestration/
│   ├── infrastructure/
│   │   ├── windows/
│   │   ├── storage/
│   │   ├── logging/
│   │   └── exporting/
│   ├── ui/
│   │   ├── windows/
│   │   ├── pages/
│   │   ├── dialogs/
│   │   └── widgets/
│   └── config/
├── data/
├── docs/
│   ├── blueprint/
│   ├── decisions/
│   └── user-guide/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── ui/
├── scripts/
└── README.md
```

This is a target shape, not a requirement to rename all current files
immediately. Installed user data should live in an appropriate per-user
application-data location, not inside the application installation
folder.

## Domain concepts

Preserve existing sound concepts such as diagnostic statuses/results,
repair risks/actions/results and sessions. Potential future models
include: - `DiagnosticProfile` - `DiagnosticFinding` with evidence,
severity, confidence and explanation - `RepairPlan` as a proposal, not
automatic execution - `DeviceRecord` - `Session` - `Report` - `UserMode`

Use stable identifiers and explicit schema versions for persisted data.

## Application service concepts

-   `DiagnosticService.run_profile(profile_id)`
-   `DiagnosticService.run_check(check_id)`
-   `RepairService.preview(action_id)`
-   `RepairService.execute(action_id, confirmation, options)`
-   `SessionService.list_sessions()`
-   `SessionService.load_session(session_id)`
-   `ReportService.export_session(session_id, format, destination)`

These are conceptual interfaces; final signatures follow code review.

## Responsiveness

Long-running work must not run on the GUI thread. Use a worker/task
mechanism and report progress, messages, warnings, completion and
cancellation. Cancellation must be cooperative; do not terminate a
process if that may leave Windows inconsistent.

## Error handling

Handle expected OS and permission errors at adapter boundaries. Return
structured results for expected failures. Preserve technical details in
logs, show understandable UI messages, never convert exceptions into
`PASS`, and distinguish unsupported data, access denied, unavailable
information and actual faults.

## Persistence

Version saved-session schemas, validate data when loading, handle older
optional fields, and migrate existing JSON carefully. Consider SQLite
only when indexing or relational needs justify it.

## Architecture decision records

Store important choices in `docs/decisions/`, e.g. UI framework,
persistence format, Windows support baseline, packaging and installer.
Each record should include context, options, decision, consequences and
date.
