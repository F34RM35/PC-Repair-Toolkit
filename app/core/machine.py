import platform

from app.diagnostics.system import get_system_info
from app.diagnostics.memory import get_memory_info
from app.diagnostics.storage import get_storage_info


def identify_windows(os_version):
    """
    Identify the Windows marketing version from the Windows build number.
    """

    if not os_version:
        return "Windows"

    try:
        parts = os_version.split(".")

        build = int(parts[2])

        if build >= 22000:
            return "Windows 11"

        return "Windows 10"

    except (ValueError, IndexError):
        return "Windows"


def get_machine_info():
    system = get_system_info()

    memory = get_memory_info()
    storage = get_storage_info()

    operating_system = system.get(
        "operating_system",
        "Unknown"
    )

    os_version = system.get(
        "os_version",
        "Unknown"
    )

    if operating_system == "Windows":
        friendly_os = identify_windows(os_version)
    else:
        friendly_os = operating_system

    machine = {
        "hostname": system.get("hostname"),
        "operating_system": friendly_os,
        "os_release": system.get("os_release"),
        "os_version": os_version,
        "architecture": system.get("architecture"),
        "processor": system.get("processor"),
        "memory": memory,
        "storage": storage,
    }

    return machine