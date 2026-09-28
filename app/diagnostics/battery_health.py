from app.core.result import DiagnosticResult, DiagnosticStatus


def analyze_battery(battery):
    name = battery.get("name") or "Unknown Battery"

    charge = battery.get("charge_percent")
    runtime = battery.get("runtime_minutes")
    status = battery.get("status")

    design_capacity = battery.get("design_capacity")
    full_charge_capacity = battery.get("full_charge_capacity")

    messages = []

    # Check whether Windows provided enough capacity information
    if design_capacity is None or full_charge_capacity is None:
        messages.append(
            "Battery capacity health data is not available from Windows."
        )

        if charge is not None:
            messages.append(
                f"Current charge: {charge}%."
            )

        if runtime is not None:
            messages.append(
                f"Estimated runtime: {runtime} minutes."
            )

        return DiagnosticResult(
            name=name,
            status=DiagnosticStatus.UNKNOWN,
            data=battery,
            message=" ".join(messages)
        )

    # Calculate battery health when capacity information is available
    if design_capacity <= 0:
        return DiagnosticResult(
            name=name,
            status=DiagnosticStatus.UNKNOWN,
            data=battery,
            message="Invalid design capacity reported."
        )

    health_percent = (
        full_charge_capacity / design_capacity
    ) * 100

    messages.append(
        f"Battery health estimate: {health_percent:.1f}%."
    )

    if health_percent < 50:
        result_status = DiagnosticStatus.CRITICAL

    elif health_percent < 80:
        result_status = DiagnosticStatus.WARNING

    else:
        result_status = DiagnosticStatus.PASS

    return DiagnosticResult(
        name=name,
        status=result_status,
        data={
            **battery,
            "health_percent": round(health_percent, 1)
        },
        message=" ".join(messages)
    )