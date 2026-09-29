from app.core.session_storage import (
    list_sessions,
    load_session,
)


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
    return input(
        "Select an option: "
    ).strip()


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
        print(
            f"{index}. {session_file.stem}"
        )

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
        print(
            f"{index}. {session_file.stem}"
        )

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

        report = load_session(
            session_id
        )

        session = report.get(
            "session",
            {}
        )

        machine = session.get(
            "machine",
            {}
        )

        summary = report.get(
            "summary",
            {}
        )

        print()
        print("=" * 60)
        print("             REPAIR SESSION")
        print("=" * 60)

        print()
        print(
            f"Session ID: "
            f"{session.get('session_id')}"
        )

        print(
            f"Started:    "
            f"{session.get('started_at')}"
        )

        print()
        print("MACHINE")
        print("-" * 60)

        print(
            f"Hostname:     "
            f"{machine.get('hostname')}"
        )

        print(
            f"OS:           "
            f"{machine.get('operating_system')}"
        )

        print(
            f"OS Build:     "
            f"{machine.get('os_version')}"
        )

        print(
            f"Architecture: "
            f"{machine.get('architecture')}"
        )

        print()
        print("DIAGNOSTIC SUMMARY")
        print("-" * 60)

        print(
            f"Total:     "
            f"{summary.get('total', 0)}"
        )

        print(
            f"PASS:      "
            f"{summary.get('pass', 0)}"
        )

        print(
            f"WARNING:   "
            f"{summary.get('warning', 0)}"
        )

        print(
            f"CRITICAL:  "
            f"{summary.get('critical', 0)}"
        )

        print(
            f"UNKNOWN:   "
            f"{summary.get('unknown', 0)}"
        )

        print()
        print("DIAGNOSTICS")
        print("-" * 60)

        diagnostics = report.get(
            "diagnostics",
            []
        )

        if not diagnostics:

            print()
            print("No diagnostic results recorded.")

        else:

            for diagnostic in diagnostics:

                print(
                    f"{diagnostic.get('name', 'Unknown'):<20}"
                    f"{diagnostic.get('status', 'UNKNOWN')}"
                )

                message = diagnostic.get(
                    "message"
                )

                if message:

                    print(
                        f"    {message}"
                    )

        # ----------------------------------------------------
        # REPAIR HISTORY
        # ----------------------------------------------------

        print()
        print("REPAIR HISTORY")
        print("-" * 60)

        repairs = session.get(
            "repairs",
            []
        )

        if not repairs:

            print()
            print(
                "No repair actions were performed."
            )

        else:

            print()

            for index, repair in enumerate(
                repairs,
                start=1
            ):

                print(
                    f"{index}. "
                    f"{repair.get('name', 'Unknown Repair')}"
                )

                print(
                    f"   Risk:       "
                    f"{repair.get('risk', 'UNKNOWN')}"
                )

                print(
                    f"   Status:     "
                    f"{repair.get('status', 'UNKNOWN')}"
                )

                print(
                    f"   Started:    "
                    f"{repair.get('started_at', 'Unknown')}"
                )

                print(
                    f"   Completed:  "
                    f"{repair.get('completed_at', 'Unknown')}"
                )

                print(
                    f"   Duration:   "
                    f"{repair.get('duration_seconds', 'Unknown')} "
                    f"seconds"
                )

                message = repair.get(
                    "message"
                )

                if message:

                    print(
                        f"   Message:    "
                        f"{message}"
                    )

                data = repair.get(
                    "data"
                )

                if isinstance(
                    data,
                    dict
                ):

                    print()
                    print(
                        "   Result:"
                    )

                    for key, value in data.items():

                        print(
                            f"   {key}: {value}"
                        )

                elif data is not None:

                    print()
                    print(
                        f"   Result:     {data}"
                    )

                error = repair.get(
                    "error"
                )

                if error:

                    print()
                    print(
                        f"   Error:      "
                        f"{error}"
                    )

                print()

        print()
        print("=" * 60)

    except Exception as error:

        print()
        print(
            f"Unable to load session: {error}"
        )


def show_repair_menu(manager):

    print()
    print("=" * 60)
    print("             REPAIR ACTIONS")
    print("=" * 60)

    actions = manager.list_actions()

    if not actions:

        print()
        print(
            "No repair actions are currently available."
        )

        return None

    print()

    for index, action in enumerate(
        actions,
        start=1
    ):

        print(
            f"{index}. {action.name}"
        )

        print(
            f"   Risk: {action.risk.value}"
        )

        print(
            f"   {action.description}"
        )

        print()

    print("0. Return")
    print()

    choice = input(
        "Select a repair action: "
    ).strip()

    if choice == "0":
        return None

    try:

        index = int(choice) - 1

        if index < 0 or index >= len(actions):

            print()
            print(
                "Invalid repair action."
            )

            return None

    except ValueError:

        print()
        print(
            "Please enter a valid number."
        )

        return None

    action = actions[index]

    print()
    print("=" * 60)
    print("             REPAIR ACTION")
    print("=" * 60)

    print()
    print(
        f"Action:      "
        f"{action.name}"
    )

    print(
        f"Risk level:  "
        f"{action.risk.value}"
    )

    print(
        f"Description: "
        f"{action.description}"
    )

    print()

    if action.risk.value != "READ_ONLY":

        confirmation = input(
            "This action can modify the system. "
            "Continue? [y/N]: "
        ).strip().lower()

        if confirmation != "y":

            print()
            print(
                "Repair cancelled."
            )

            return None

    print()
    print(
        "Running repair action..."
    )

    result = manager.run(
        action
    )

    print()
    print("RESULT")
    print("-" * 60)

    print(
        f"Status:  "
        f"{result.status.value}"
    )

    print(
        f"Message: "
        f"{result.message}"
    )

    if result.data:

        print()
        print("DATA")
        print("-" * 60)

        if isinstance(
            result.data,
            dict
        ):

            for key, value in result.data.items():

                print(
                    f"{key}: {value}"
                )

        else:

            print(
                result.data
            )

    if result.error:

        print()
        print(
            f"Error: {result.error}"
        )

    print()
    print("=" * 60)

    return result