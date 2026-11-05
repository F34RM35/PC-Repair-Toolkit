# Product Vision and Requirements

## Vision

PC Repair Toolkit is intended to become a professional Windows desktop
application that helps people understand, diagnose, maintain and
troubleshoot Windows computers. It combines a capable diagnostic and
repair engine with an interface that makes findings understandable.

It serves three audiences through one application: 1. Everyday users
with little technical knowledge. 2. PC enthusiasts who want detail and
control. 3. IT technicians and repair businesses who need efficient
diagnostics, traceable actions and useful reports.

**Principle: Complex engineering underneath; clear experiences on the
surface.**

## Product goals

-   Identify and explain common hardware, software and Windows
    configuration problems.
-   Present diagnostic information with clear confidence and
    limitations.
-   Offer appropriate repairs with safeguards.
-   Preserve diagnostic sessions and repair history.
-   Help users learn what a finding means and what they can safely do
    next.
-   Support advanced investigation without overwhelming beginners.
-   Be maintainable, testable, secure and suitable for eventual
    commercial distribution.

## Initial non-goals

V1.0 should not attempt to replace specialist test equipment, guarantee
component health from software readings, automatically repair every
issue, perform unattended destructive changes, provide remote repair,
act as antivirus software, or support every Windows version from day
one.

## Experience modes

### Beginner

-   One-click basic health scan.
-   Plain-English summaries.
-   Explain what a finding means and why it matters.
-   Separate confirmed issues from warnings and unavailable information.
-   Guided instructions and conservative maintenance actions.
-   Explain the effect before asking the user to approve a change.

### Advanced

-   Detailed diagnostic output and hardware information.
-   Expanded tests and analysis.
-   Advanced repair options where supported.
-   Access to logs and technical details.
-   Clear indication when administrator privileges are required.

### Technician

-   Comprehensive diagnostic profiles.
-   Device/session history.
-   Customer and device labelling subject to privacy controls.
-   Professional report generation.
-   Repair action audit trail and detailed evidence.
-   Configurable report sections.

Modes change detail and workflow, not fundamental safety controls.
Technician mode is not a certification claim.

## Proposed application areas

  -----------------------------------------------------------------------
  Area                    Purpose                 Priority
  ----------------------- ----------------------- -----------------------
  Dashboard               Device health and       High
                          recent activity         

  Diagnostics             Individual tests and    High
                          full scans              

  Repair Centre           Guided maintenance and  High
                          repair                  

  Hardware                Component and system    High
                          information             

  Storage                 Capacity and disk       High
                          analysis                

  Network                 Connectivity and        Medium
                          configuration checks    

  Windows Tools           Servicing and           Medium
                          troubleshooting helpers 

  Reports & History       Sessions, repair        High
                          history and exports     

  Settings                Preferences, privacy    High
                          and modes               

  Technician workspace    Device labels, notes    Later
                          and professional        
                          workflows               
  -----------------------------------------------------------------------

## Functional requirements

### Diagnostics

-   Run full profiles and individual checks.
-   Show progress and isolate failures so one check does not crash the
    scan.
-   Record timestamp, device context, status and evidence.
-   Distinguish `PASS`, `WARNING`, `CRITICAL` and `UNKNOWN`.
-   Explain unavailable information rather than treating it as a
    failure.

### Repairs

-   Explain purpose, expected effect and risk.
-   Require explicit confirmation for system changes.
-   Request elevation only when genuinely required.
-   Record start/end time, result, output, skips and failures.
-   Handle partial success, cancellation and failure.
-   Verify the resulting state where practical.
-   Never claim success just because a command launched.

### Reports and history

-   Save and reopen sessions.
-   Show diagnostics and repair actions together.
-   Export PDF and JSON.
-   Avoid sensitive data in exports by default.
-   Support redaction before sharing.

### Finding explanations

Where evidence supports it, show what was detected, what it means,
severity, confidence, possible impact, recommended next step, available
repair and known limitations.

## Quality requirements

-   No unhandled exception should terminate normal workflows.
-   Long-running tasks must not freeze the interface.
-   Core logic must be testable without the GUI.
-   Repair actions need tests for success, failure and cancellation
    where practical.
-   Logs must be useful without exposing unnecessary personal data.
-   Compatibility claims must match actual testing.

## Success measures

Successful installation on supported Windows systems; valid saved
sessions; correct report exports; accurate repair outcomes;
understandable findings for beginners; useful evidence for technicians;
and no unresolved critical data-loss or privilege-escalation defects at
release.
