import subprocess
import json


def get_battery_info():
    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        """
        Get-CimInstance Win32_Battery |
        Select-Object DeviceID, Name, BatteryStatus,
        EstimatedChargeRemaining, EstimatedRunTime,
        DesignCapacity, FullChargeCapacity |
        ConvertTo-Json
        """
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=15
        )

        if result.returncode != 0:
            return []

        output = result.stdout.strip()

        if not output:
            return []

        data = json.loads(output)

        if isinstance(data, dict):
            data = [data]

        batteries = []

        for battery in data:
            batteries.append({
                "device_id": battery.get("DeviceID"),
                "name": battery.get("Name"),
                "status": battery.get("BatteryStatus"),
                "charge_percent": battery.get(
                    "EstimatedChargeRemaining"
                ),
                "runtime_minutes": battery.get(
                    "EstimatedRunTime"
                ),
                "design_capacity": battery.get(
                    "DesignCapacity"
                ),
                "full_charge_capacity": battery.get(
                    "FullChargeCapacity"
                ),
            })

        return batteries

    except (
        subprocess.SubprocessError,
        json.JSONDecodeError,
        ValueError,
        TypeError
    ):
        return []