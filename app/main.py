from app.core.diagnostic_manager import DiagnosticManager
from app.core.result import DiagnosticStatus
from app.core.session import create_session
from app.core.machine import get_machine_info
from app.reporting.report_builder import build_report
from app.core.session_storage import save_session

from app.core.repair import RepairAction, RepairRisk
from app.core.repair_manager import RepairManager
from app.core.repairs import analyze_temp_files

from app.ui.menu import (
    show_header,
    show_menu,
    show_sessions,
    open_session,
    show_repair_menu,
)


def create_repair_manager():
    manager = RepairManager()

    manager.register(
        RepairAction(
            name="Temporary File Analysis",
            risk=RepairRisk.READ_ONLY,
            description=(
                "Analyze Windows temporary files "
                "without deleting anything."
            ),
            function=analyze_temp_files,
        )
    )

    return manager


def run_diagnostic():
    print()
    print("=" * 60)
    print("             NEW DIAGNOSTIC")
    print("=" * 60)

    machine = get_machine_info()
    session = create_session(machine)

    manager = DiagnosticManager()

    print()
    print("REPAIR SESSION")
    print("-" * 60)
    print(f"Session ID: {session['session_id']}")
    print(f"Started:    {session['started_at']}")

    print()
    print("MACHINE")
    print("-" * 60)
    print(f"Hostname:     {machine['hostname']}")
    print(f"OS:           {machine['operating_system']}")
    print(f"OS Build:     {machine['os_version']}")
    print(f"Architecture: {machine['architecture']}")

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

    report = build_report(
        results,
        session
    )

    saved_file = save_session(
        report
    )

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
    print(f"Report saved: {saved_file}")

    print()
    print("=" * 60)
    print("             DIAGNOSTIC COMPLETE")
    print("=" * 60)

    repair_manager = create_repair_manager()

    print()
    show_repair_menu(repair_manager)


def main():

    while True:

        show_header()
        show_menu()

        choice = input(
            "Select an option: "
        ).strip()

        if choice == "1":

            run_diagnostic()

            input(
                "\nPress Enter to return to the main menu..."
            )

        elif choice == "2":

            show_sessions()

            input(
                "\nPress Enter to return to the main menu..."
            )

        elif choice == "3":

            open_session()

            input(
                "\nPress Enter to return to the main menu..."
            )

        elif choice == "4":

            print()
            print("Exiting PC Repair Toolkit...")
            break

        else:

            print()
            print("Invalid option. Please select 1-4.")


if __name__ == "__main__":
    main()