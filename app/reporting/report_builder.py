from datetime import datetime
from dataclasses import asdict, is_dataclass
from enum import Enum

from app.core.result import DiagnosticStatus


def make_json_safe(value):
    """
    Convert diagnostic data into values that can be saved as JSON.
    """

    if is_dataclass(value):
        return make_json_safe(asdict(value))

    if isinstance(value, Enum):
        return value.value

    if isinstance(value, dict):
        return {
            str(key): make_json_safe(item)
            for key, item in value.items()
        }

    if isinstance(value, (list, tuple)):
        return [
            make_json_safe(item)
            for item in value
        ]

    if isinstance(value, (str, int, float, bool)) or value is None:
        return value

    return str(value)


def build_report(results, session=None):
    report = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "session": make_json_safe(session),
        "diagnostics": [],
        "summary": {
            "total": 0,
            "pass": 0,
            "warning": 0,
            "critical": 0,
            "unknown": 0
        }
    }

    for result in results.values():

        status = result.status

        diagnostic = {
            "name": result.name,
            "status": status.value,
            "message": result.message,
            "data": make_json_safe(result.data),
            "error": result.error
        }

        report["diagnostics"].append(diagnostic)
        report["summary"]["total"] += 1

        if status == DiagnosticStatus.PASS:
            report["summary"]["pass"] += 1

        elif status == DiagnosticStatus.WARNING:
            report["summary"]["warning"] += 1

        elif status == DiagnosticStatus.CRITICAL:
            report["summary"]["critical"] += 1

        elif status == DiagnosticStatus.UNKNOWN:
            report["summary"]["unknown"] += 1

    return report