from app.core.session_storage import (
    list_sessions,
    load_session
)


def main():

    print()
    print("=" * 60)
    print("SAVED REPAIR SESSIONS")
    print("=" * 60)

    sessions = list_sessions()

    if not sessions:
        print()
        print("No saved sessions found.")
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
    print("-" * 60)

    latest_file = sessions[0]

    session_id = latest_file.stem

    report = load_session(session_id)

    session = report.get("session", {})
    machine = session.get("machine", {})
    summary = report.get("summary", {})

    print()
    print("LATEST SESSION")
    print("-" * 60)

    print(
        f"Session ID: {session.get('session_id')}"
    )

    print(
        f"Started:    {session.get('started_at')}"
    )

    print(
        f"Hostname:   {machine.get('hostname')}"
    )

    print(
        f"OS:         {machine.get('operating_system')}"
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
    print("=" * 60)


if __name__ == "__main__":
    main()