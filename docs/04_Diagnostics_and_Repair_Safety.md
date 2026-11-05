# Diagnostics and Repair Safety

## Purpose

The toolkit must help without putting files, Windows or hardware at
unnecessary risk. Safety is a product requirement.

## Diagnostic statuses

  Status     Meaning
  ---------- ---------------------------------------------------------
  PASS       Check ran and found no issue under its defined criteria
  WARNING    A condition may need attention
  CRITICAL   A serious issue was detected under defined criteria
  UNKNOWN    The check could not reach a reliable conclusion

`UNKNOWN` is neither `PASS` nor `CRITICAL`. Explain whether the cause
was unsupported hardware, missing sensor data, insufficient permissions
or another limitation.

## Evidence and confidence

Where possible, every finding should include check ID/version,
timestamp, structured evidence, interpretation, severity, confidence,
limitations and recommended next step. Do not diagnose a failing
component from one indirect signal.

## Repair risk model

  -----------------------------------------------------------------------
  Risk                    Description             Control
  ----------------------- ----------------------- -----------------------
  READ_ONLY               Inspects without        No modification
                          changing system state   confirmation

  SAFE                    Limited change with low Explain and obtain
                          expected risk           explicit confirmation

  ELEVATED                Requires admin rights   Explain, confirm,
                          or changes important    elevate only when
                          configuration           needed

  DESTRUCTIVE             Can remove data or      Strong warning,
                          cause                   explicit confirmation
                          difficult-to-reverse    and recovery guidance;
                          changes                 exclude from early
                                                  releases unless
                                                  justified
  -----------------------------------------------------------------------

Assign risk based on actual effects, not reassuring wording.

## Repair lifecycle

1.  Check prerequisites.
2.  Inspect current state.
3.  Preview intended changes where practical.
4.  Explain impact and risk.
5.  Obtain confirmation.
6.  Request elevation only if required.
7.  Execute.
8.  Capture output, errors, skips and changes.
9.  Verify resulting state.
10. Save a structured result.

If verification cannot prove the change occurred, report the limitation
instead of claiming success.

## Safety rules

-   Never silently execute a system-changing repair.
-   Never delete user documents or personal files as general cleanup.
-   Prefer documented Windows servicing procedures over manually
    deleting protected system data.
-   Check update/servicing activity before touching Windows Update
    cache.
-   Do not disable security protections to make a repair easier.
-   Do not build shell commands from untrusted input.
-   Validate paths and options.
-   Use least privilege.
-   Provide cancellation where safe.
-   Record partial completion accurately.
-   Do not automatically retry destructive actions.
-   Do not claim a restore point or backup exists unless verified.

## Existing V0.1 actions

-   Temporary File Analysis --- READ_ONLY.
-   Disk Cleanup Analysis --- READ_ONLY.
-   Clean Windows Update Cache --- currently labelled SAFE;
    implementation and servicing behaviour require further review before
    commercial release.
-   Clean Temporary Files --- SAFE.

On 5 November 2026, temporary cleanup reported 113 files found, 102
deleted, 11 skipped, 42 directories removed and 50.17 MB deleted. This
is one successful test, not proof across all Windows installations.

A large Windows Update cache folder does not prove every item is safe to
delete. Check servicing activity, use supported procedures, and test in
disposable VMs before release.

## Testing

For diagnostics, test normal results, missing data, unsupported devices,
access denied, unexpected output, timeout and malformed data.

For repairs, test preview, declined confirmation, success, partial
success, in-use files, access denied, cancellation, exceptions and
verification mismatch.

Use mocks for unit tests and disposable VMs for integration tests. Do
not use important production computers as the first test target for new
repair actions.

## Release gate

An action is not releasable until purpose, scope and risk are
documented; inputs are validated; permissions and failures are handled;
results are accurate; tests pass; and user-facing explanations are
clear.
