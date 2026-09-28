from app.core.session_storage import list_sessions, load_session


def show_header():
    print()
    print("=" * 60)
    print("             PC REPAIR TOOLKIT")
    print("                    V0.1")
    print("=" * 60)


def show_menu():
    print()
    print("1. Run New Diagnostic")
    print("2. View Previous Sessions")
    print("3. Open Session")
    print("4. Exit")
    print()


def get_choice():
    return input("Select an option: ").strip()


def show_sessions():
    sessions = list_sessions()

    print()
    print("=" * 60)
    print("             PREVIOUS SESSIONS")
    print("=" * 60)

    if not sessions:
        print()
        print("No saved repair sessions.")
        return

    print()

    for index, session_file in enumerate(
        sessions,
        start=1
    ):
        print(f"{index}. {session_file.stem}")

    print()


def open_session():
    sessions = list_sessions()

    if not sessions:
        print()
        print("No saved repair sessions.")
        return

    print()
    print("=" * 60)
    print("             OPEN SESSION")
    print("=" * 60)

    print()

    for index, session_file in enumerate(
        sessions,
        start=1
    ):
        print(f"{index}. {session_file.stem}")

    print()
    print("Enter the session number or full Session ID.")
    print()

    choice = input(
        "Select session: "
    ).strip()

    selected_file = None

    # Try selecting by number first
    try:
        index = int(choice) - 1

        if 0 <= index < len(sessions):
            selected_file = sessions[index]

    except ValueError:
        pass

    # If it wasn't a number, try Session ID
    if selected_file is None:

        for session_file in sessions:

            if session_file.stem.lower() == choice.lower():
                selected_file = session_file
                break

    if selected_file is None:
        print()
        print("Session not found.")
        return

    session_id = selected_file.stem

    try:
        report = load_session(session_id)

        session = report.get("session", {})
        machine = session.get("machine", {})
        summary = report.get("summary", {})

        print()
        print("=" * 60)
        print("             REPAIR SESSION")
        print("=" * 60)

        print()
        print(f"Session ID: {session.get('session_id')}")
        print(f"Started:    {session.get('started_at')}")

        print()
        print("MACHINE")
        print("-" * 60)

        print(
            f"Hostname:     {machine.get('hostname')}"
        )

        print(
            f"OS:           {machine.get('operating_system')}"
        )

        print(
            f"OS Build:     {machine.get('os_version')}"
        )

        print(
            f"Architecture: {machine.get('architecture')}"
        )

        print()
        print("DIAGNOSTIC SUMMARY")
        print("-" * 60)

        print(
            f"Total:     {summary.get('total', 0)}"
        )

        print(
            f"PASS:      {summary.get('pass', 0)}"
        )

        print(
            f"WARNING:   {summary.get('warning', 0)}"
        )

        print(
            f"CRITICAL:  {summary.get('critical', 0)}"
        )

        print(
            f"UNKNOWN:   {summary.get('unknown', 0)}"
        )

        print()
        print("DIAGNOSTICS")
        print("-" * 60)

        for diagnostic in report.get(
            "diagnostics",
            []
        ):
            print(
                f"{diagnostic.get('name'):<20}"
                f"{diagnostic.get('status')}"
            )

        print()
        print("=" * 60)

    except Exception as error:
        print()
        print(
            f"Unable to load session: {error}"
        )