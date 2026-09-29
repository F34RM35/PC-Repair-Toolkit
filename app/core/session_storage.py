import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

SESSIONS_DIR = BASE_DIR / "data" / "sessions"


def save_session(report):
    """
    Save a repair session as a JSON file.

    The report is first written to a temporary file.
    Only after the write succeeds is it moved into place.
    This prevents partially-written session files.
    """

    SESSIONS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    session = report.get("session")

    if not session:
        raise ValueError(
            "Report does not contain a repair session."
        )

    session_id = session.get("session_id")

    if not session_id:
        raise ValueError(
            "Repair session does not contain a session ID."
        )

    file_path = SESSIONS_DIR / f"{session_id}.json"
    temp_path = SESSIONS_DIR / f"{session_id}.tmp"

    try:
        with temp_path.open(
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report,
                file,
                indent=4,
                ensure_ascii=False
            )

            file.flush()

        temp_path.replace(file_path)

    except Exception:

        if temp_path.exists():
            temp_path.unlink()

        raise

    return file_path


def list_sessions():
    """
    Return all saved repair session files.
    """

    if not SESSIONS_DIR.exists():
        return []

    return sorted(
        SESSIONS_DIR.glob("*.json"),
        reverse=True
    )


def load_session(session_id):
    """
    Load a saved repair session by session ID.
    """

    file_path = SESSIONS_DIR / f"{session_id}.json"

    if not file_path.exists():
        raise FileNotFoundError(
            f"Repair session not found: {session_id}"
        )

    with file_path.open(
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def update_session(session_id, report):
    """
    Update an existing repair session.

    Uses the same safe temporary-file replacement
    mechanism as save_session().
    """

    if not session_id:
        raise ValueError(
            "Session ID is required."
        )

    if not isinstance(report, dict):
        raise TypeError(
            "Report must be a dictionary."
        )

    session = report.get("session")

    if not session:
        raise ValueError(
            "Report does not contain a repair session."
        )

    report_session_id = session.get("session_id")

    if report_session_id != session_id:
        raise ValueError(
            "Session ID does not match report."
        )

    SESSIONS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = SESSIONS_DIR / f"{session_id}.json"
    temp_path = SESSIONS_DIR / f"{session_id}.tmp"

    try:

        with temp_path.open(
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report,
                file,
                indent=4,
                ensure_ascii=False
            )

            file.flush()

        temp_path.replace(file_path)

    except Exception:

        if temp_path.exists():
            temp_path.unlink()

        raise

    return file_path