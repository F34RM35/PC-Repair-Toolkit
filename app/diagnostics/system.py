import getpass
import platform
import socket


def get_system_info():
    return {
        "hostname": socket.gethostname(),
        "username": getpass.getuser(),
        "operating_system": platform.system(),
        "os_release": platform.release(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
    }