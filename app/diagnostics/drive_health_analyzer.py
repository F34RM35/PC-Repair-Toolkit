from app.core.result import DiagnosticResult, DiagnosticStatus


def analyze_drive_health(drive):
    if not drive:
        return DiagnosticResult(
            name="Drive Health",
            status=DiagnosticStatus.UNKNOWN,
            data=None,
            message="No drive health information available."
        )

    health = str(drive.get("health", "")).lower()
    status = str(drive.get("status", "")).lower()

    name = drive.get("name", "Unknown drive")
    media_type = drive.get("media_type", "Unknown")
    size_gb = drive.get("size_gb", "Unknown")

    if health == "healthy" and status == "ok":
        return DiagnosticResult(
            name="Drive Health",
            status=DiagnosticStatus.PASS,
            data=drive,
            message=(
                f"{name} reports healthy. "
                f"Type: {media_type}. "
                f"Capacity: {size_gb} GB."
            )
        )

    if health in ("warning", "caution") or status in ("warning", "degraded"):
        return DiagnosticResult(
            name="Drive Health",
            status=DiagnosticStatus.WARNING,
            data=drive,
            message=(
                f"{name} reports a drive health warning. "
                f"Health: {drive.get('health')}. "
                f"Status: {drive.get('status')}."
            )
        )

    if health in ("critical", "failed", "failure") or status in (
        "critical",
        "failed",
        "failure"
    ):
        return DiagnosticResult(
            name="Drive Health",
            status=DiagnosticStatus.CRITICAL,
            data=drive,
            message=(
                f"{name} reports a critical drive health condition. "
                f"Health: {drive.get('health')}. "
                f"Status: {drive.get('status')}."
            )
        )

    return DiagnosticResult(
        name="Drive Health",
        status=DiagnosticStatus.UNKNOWN,
        data=drive,
        message=(
            f"{name} returned drive health information, "
            f"but the health status could not be confidently classified."
        )
    )