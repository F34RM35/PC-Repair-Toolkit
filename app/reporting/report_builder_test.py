from app.core.diagnostic_manager import DiagnosticManager
from app.reporting.report_builder import build_report


def main():

    manager = DiagnosticManager()

    print()
    print("=" * 60)
    print("REPORT BUILDER TEST")
    print("=" * 60)

    results = manager.run_all()

    report = build_report(results)

    print()
    print("TIMESTAMP")
    print("-" * 60)
    print(report["timestamp"])

    print()
    print("SUMMARY")
    print("-" * 60)

    summary = report["summary"]

    print(f"Total:     {summary['total']}")
    print(f"PASS:      {summary['pass']}")
    print(f"WARNING:   {summary['warning']}")
    print(f"CRITICAL:  {summary['critical']}")
    print(f"UNKNOWN:   {summary['unknown']}")

    print()
    print("DIAGNOSTICS")
    print("-" * 60)

    for diagnostic in report["diagnostics"]:
        print(
            f"{diagnostic['name']}: "
            f"{diagnostic['status']}"
        )

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()