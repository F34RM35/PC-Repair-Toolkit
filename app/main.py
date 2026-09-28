from app.core.diagnostic_manager import DiagnosticManager
from app.core.result import DiagnosticStatus


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

        print(f"{symbol} {result.name:<20} {result.status.value}")

        if result.status != DiagnosticStatus.PASS:
            if result.message:
                print(f"    └─ {result.message}")

        if result.error:
            print(f"    Error: {result.error}")

    print()
    print("=" * 60)
    print("             DIAGNOSTIC COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()