from app.core.result import DiagnosticResult, DiagnosticStatus


def analyze_storage(drive):
    device = drive.get("device", "Unknown")
    total_gb = drive.get("total_gb")
    used_gb = drive.get("used_gb")
    free_gb = drive.get("free_gb")
    usage_percent = drive.get("usage_percent")

    if usage_percent is None:
        return DiagnosticResult(
            name=device,
            status=DiagnosticStatus.UNKNOWN,
            data=drive,
            message="Storage usage information is unavailable."
        )

    # Critical: extremely little free space
    if usage_percent >= 95:
        status = DiagnosticStatus.CRITICAL
        message = (
            f"{device} is critically full at "
            f"{usage_percent:.1f}% usage."
        )

    # Warning: storage is getting very full
    elif usage_percent >= 90:
        status = DiagnosticStatus.WARNING
        message = (
            f"{device} is running low on free space at "
            f"{usage_percent:.1f}% usage."
        )

    # Healthy amount of free space
    else:
        status = DiagnosticStatus.PASS
        message = (
            f"{device} has sufficient free space at "
            f"{usage_percent:.1f}% usage."
        )

    return DiagnosticResult(
        name=device,
        status=status,
        data={
            "device": device,
            "total_gb": total_gb,
            "used_gb": used_gb,
            "free_gb": free_gb,
            "usage_percent": usage_percent
        },
        message=message
    )