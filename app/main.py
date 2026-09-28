from app.core.diagnostic_manager import DiagnosticManager
from app.core.result import DiagnosticStatus
from app.reporting.report_builder import build_report


def main():
    print("=" * 60)
    print("             PC REPAIR TOOLKIT")
    print("                    V0.1")
    print("=" * 60)

    manager = DiagnosticManager()

    print()
    print("Running diagnostics...")
    print()

    results = manager.run_all()

    # Display diagnostic results
    for result in results.values():

        if result.status == DiagnosticStatus.PASS:
            symbol = "[✓]"

        elif result.status == DiagnosticStatus.WARNING:
            symbol = "[!]"

        elif result.status == DiagnosticStatus.CRITICAL:
            symbol = "[X]"

        elif result.status == DiagnosticStatus.UNKNOWN:
            symbol = "[?]"

        else:
            symbol = "[?]"

        print(
            f"{symbol} "
            f"{result.name:<20} "
            f"{result.status.value}"
        )

        if result.status != DiagnosticStatus.PASS:
            if result.message:
                print(
                    f"    └─ {result.message}"
                )

    # Build structured diagnostic report
    report = build_report(results)

    print()
    print("=" * 60)
    print("             DIAGNOSTIC SUMMARY")
    print("=" * 60)

    summary = report["summary"]

    print(f"Total Diagnostics: {summary['total']}")
    print(f"PASS:              {summary['pass']}")
    print(f"WARNING:           {summary['warning']}")
    print(f"CRITICAL:          {summary['critical']}")
    print(f"UNKNOWN:           {summary['unknown']}")

    print()
    print("=" * 60)
    print("             DIAGNOSTIC COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()