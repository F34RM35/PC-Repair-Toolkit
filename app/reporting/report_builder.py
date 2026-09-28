from datetime import datetime
from app.core.result import DiagnosticStatus


def build_report(results):
    report = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
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
            "data": result.data,
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