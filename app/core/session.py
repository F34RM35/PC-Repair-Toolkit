from datetime import datetime
import uuid


def create_session(machine=None):
    now = datetime.now()

    session_id = (
        f"PRK-{now.strftime('%Y%m%d-%H%M')}-"
        f"{uuid.uuid4().hex[:6].upper()}"
    )

    return {
    "session_id": session_id,
    "started_at": now.isoformat(timespec="seconds"),
    "machine": machine,
    "repairs": []
}