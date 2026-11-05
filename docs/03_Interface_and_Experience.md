# Interface and Experience

## Principles

-   Make the next useful action obvious.
-   Use plain language first and technical detail on demand.
-   Never imply more certainty than the evidence supports.
-   Keep navigation consistent across modes.
-   Make risky actions visibly different from read-only analysis.
-   Explain a result before asking the user to act.

## Proposed layout

``` text
┌──────────────────────────────────────────────────────────────┐
│ PC REPAIR TOOLKIT                    Mode: Beginner       ⚙  │
├───────────────┬──────────────────────────────────────────────┤
│ Dashboard     │                                              │
│ Diagnostics   │                 Main content                 │
│ Repair Centre │                                              │
│ Hardware      │       Health summary / selected page         │
│ Storage       │                                              │
│ Network       │                                              │
│ Windows Tools │                                              │
│ Reports       │                                              │
│ Settings      │                                              │
├───────────────┴──────────────────────────────────────────────┤
│ Ready • Last scan • Application version                      │
└──────────────────────────────────────────────────────────────┘
```

Build a small PySide6 prototype before committing to a detailed visual
design.

## Dashboard

Answer: Is the computer broadly operating normally? What was checked?
What needs attention? What could not be measured? What should happen
next?

Possible cards: health summary, last scan, CPU/memory, storage capacity,
drive status when available, battery data when available,
recommendations and recent repairs.

Do not invent a single health score until its calculation is explainable
and tested.

## Diagnostics

-   Full scan and individual test controls.
-   Profile selection.
-   Progress and live status.
-   Results grouped by category.
-   Expandable technical evidence.
-   Save/export actions.

## Repair Centre

Organise by temporary files, storage, Windows Update troubleshooting,
system integrity, network and startup/application troubleshooting.

Each action should show purpose, what will change, risk, elevation
requirement, preview, confirmation and final outcome.

## Reports and history

Provide searchable sessions, session details, diagnostic findings,
repair outcomes, timestamps, device context, PDF/JSON export and
optional redaction.

## Mode differences

  Capability                  Beginner            Advanced    Technician
  --------------------------- ------------------- ----------- ------------
  Plain-English summaries     Primary             Available   Available
  Technical evidence          Simplified          Expanded    Expanded
  Full and individual scans   Guided              Full        Full
  Repair explanations         Guided              Technical   Technical
  Repair controls             Conservative        Expanded    Expanded
  Session history             Simple              Detailed    Detailed
  Professional reports        Basic               Optional    Primary
  Customer/device labels      Hidden by default   Optional    Available

Mode selection is not an authorisation system. Permissions, risk checks
and confirmations apply in every mode.

## Accessibility

Support keyboard navigation, clear focus, readable/scalable text, status
labels that do not rely on colour alone, consistent terminology,
tooltips, visible progress and safe cancellation.

## Visual direction

Use a restrained professional Windows desktop style with clear
hierarchy, consistent spacing, legible typography, limited status
colours and consistent icons. Avoid decorative gauges that obscure real
information.
