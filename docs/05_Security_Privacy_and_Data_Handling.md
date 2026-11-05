# Security, Privacy and Data Handling

## Objectives

The toolkit may inspect and modify sensitive parts of Windows. It must
minimise privileges, protect local records and explain data handling.

## Least privilege

-   Run as a standard user by default.
-   Elevate only for a specific action that requires it.
-   Explain why elevation is needed.
-   Keep elevated work narrowly scoped.
-   Do not permanently require administrator privileges without a
    demonstrated need.

## Local data

Sensitive data may appear in hostnames, usernames, paths, logs,
installed software lists, network configuration, technician notes and
exported reports.

The application should: - Store only necessary information. - Use an
appropriate per-user application-data location. - Respect Windows
account permissions. - Offer report redaction. - Avoid sensitive data in
filenames. - Provide documented export and deletion processes. -
Separate sample data from real customer records.

## Encryption

Encryption at rest may be appropriate for technician/customer records.
Design must cover key creation, storage, recovery, rotation and failure
handling.

Do not invent cryptography. Use established, maintained libraries and
Windows security facilities where appropriate. Never store encryption
keys beside encrypted data in plain text.

If portable encrypted USB storage is considered later, treat it as a
distinct feature with compatibility, backup and recovery design. Saving
files to a USB drive does not itself encrypt them.

## Network and telemetry

Initial releases should work locally and not require a cloud account. -
No telemetry by default unless a privacy-reviewed opt-in is adopted. -
No diagnostic report upload without explicit user action. - No remote
control or remote repair in initial scope. - Disclose update checks and
network requests. - Do not transmit customer data in crash reports.

## Updates

When commercially feasible, sign application binaries. Verify update
packages before installation. Protect update channels, publish
version/release notes, and define rollback or recovery for failed
updates.

## Logging

Redact secrets and unnecessary personal data, use structured log levels,
set retention limits, make log export user-controlled, and never log
passwords, tokens, licence secrets or encryption keys.

## Threat modelling

Before features involving customer data, elevation, updates or remote
capability, document assets, trust boundaries, misuse cases, entry
points, privileges, mitigations and residual risks.

Security testing must use authorised environments. Do not include hidden
access, credential collection or unauthorised remote-control features.
