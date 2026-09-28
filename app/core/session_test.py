from app.core.session import create_session


def main():
    session = create_session()

    print()
    print("=" * 60)
    print("REPAIR SESSION TEST")
    print("=" * 60)

    print()
    print(f"Session ID: {session['session_id']}")
    print(f"Started:    {session['started_at']}")

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()