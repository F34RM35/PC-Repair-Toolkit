# PC Repair Toolkit --- V1.0 Blueprint

**Status:** Proposed baseline\
**Current implementation:** V0.1 command-line prototype\
**Target:** Windows desktop application\
**Audience:** Everyday Windows users, PC enthusiasts, IT technicians and
repair businesses

## Purpose

This blueprint defines the proposed product direction, requirements,
architecture, user experience, safety principles and staged delivery
plan. It is a plan, not a claim that proposed features are already
implemented.

## Document map

1.  [Product vision and
    requirements](01_Product_Vision_and_Requirements.md)
2.  [Application architecture](02_Application_Architecture.md)
3.  [Interface and experience](03_Interface_and_Experience.md)
4.  [Diagnostics and repair safety](04_Diagnostics_and_Repair_Safety.md)
5.  [Security, privacy and data
    handling](05_Security_Privacy_and_Data_Handling.md)
6.  [Development roadmap](06_Development_Roadmap.md)
7.  [Commercial considerations](07_Commercial_Product_Considerations.md)

## Recommended location

Keep these files **inside the existing PC Repair Toolkit repository** in
`docs/blueprint/`. They describe this product and should be versioned
with its source code. A separate repository is unnecessary for the
blueprint.

Suggested structure:

``` text
PC-Repair-Toolkit/
├── app/
├── data/
├── tests/
├── docs/
│   └── blueprint/
│       ├── 00_Blueprint_Index.md
│       ├── 01_Product_Vision_and_Requirements.md
│       ├── 02_Application_Architecture.md
│       ├── 03_Interface_and_Experience.md
│       ├── 04_Diagnostics_and_Repair_Safety.md
│       ├── 05_Security_Privacy_and_Data_Handling.md
│       ├── 06_Development_Roadmap.md
│       └── 07_Commercial_Product_Considerations.md
├── .gitignore
└── README.md
```

A separate repository makes sense only if the material becomes a
genuinely independent product, shared documentation for several
projects, or a separate public website. Keep the application repository
private while commercial development is confidential.

## Verified V0.1 baseline --- 5 November 2026

-   The command-line application launched successfully.
-   System, CPU, Memory and Storage diagnostics returned `PASS`.
-   Drive Health and Battery returned `UNKNOWN` because expected health
    information was unavailable; battery charge/runtime information was
    still displayed.
-   Temporary File Cleanup completed after confirmation: 113 files
    found, 102 deleted, 11 skipped, 42 directories removed and 50.17 MB
    reported deleted.
-   The session JSON was saved and the user confirmed that the session
    and reports reopened correctly.

This is a limited functional baseline, not a full compatibility or
safety certification.

## How to use this blueprint

Treat it as a proposal. Update it as decisions change, record
significant technical choices, keep V0.1 working during development, and
do not mark features complete until implemented and tested.
