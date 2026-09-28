from app.core.session import create_session
from app.core.machine import get_machine_info
from app.core.diagnostic_manager import DiagnosticManager
from app.reporting.report_builder import build_report
from app.core.session_storage import save_session


def main():

    print()
    print("=" * 60)
    print("SESSION STORAGE TEST")
    print("=" * 60)

    machine = get_machine_info()

    session = create_session(
        machine
    )

    manager = DiagnosticManager()

    results = manager.run_all()

    report = build_report(
        results,
        session
    )

    file_path = save_session(
        report
    )

    print()
    print(f"Session ID: {session['session_id']}")
    print(f"Saved to:   {file_path}")

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()