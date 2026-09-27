import subprocess
import json


def get_drive_health():
    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        """
        Get-PhysicalDisk |
        Select-Object FriendlyName, MediaType, HealthStatus, OperationalStatus, Size |
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

        drives = []

        for drive in data:
            drives.append({
                "name": drive.get("FriendlyName"),
                "media_type": drive.get("MediaType"),
                "health": drive.get("HealthStatus"),
                "status": drive.get("OperationalStatus"),
                "size_gb": round(
                    int(drive.get("Size", 0)) / (1024 ** 3),
                    2
                )
            })

        return drives

    except (
        subprocess.SubprocessError,
        json.JSONDecodeError,
        ValueError,
        TypeError
    ):
        return []