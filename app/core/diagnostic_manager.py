from app.core.result import DiagnosticResult, DiagnosticStatus

from app.diagnostics.system import get_system_info
from app.diagnostics.cpu import get_cpu_info
from app.diagnostics.memory import get_memory_info
from app.diagnostics.storage import get_storage_info
from app.diagnostics.drive_health import get_drive_health
from app.diagnostics.battery import get_battery_info


class DiagnosticManager:

    def run_all(self):
        results = {}

        results["system"] = self._run(
            "System",
            get_system_info
        )

        results["cpu"] = self._run(
            "CPU",
            get_cpu_info
        )

        results["memory"] = self._run(
            "Memory",
            get_memory_info
        )

        results["storage"] = self._run(
            "Storage",
            get_storage_info
        )

        results["drive_health"] = self._run(
            "Drive Health",
            get_drive_health
        )

        results["battery"] = self._run(
            "Battery",
            get_battery_info
        )

        return results

    def _run(self, name, function):
        try:
            data = function()

            return DiagnosticResult(
                name=name,
                status=DiagnosticStatus.PASS,
                data=data,
                message="Diagnostic completed successfully."
            )

        except Exception as error:
            return DiagnosticResult(
                name=name,
                status=DiagnosticStatus.UNKNOWN,
                data=None,
                message="Diagnostic could not be completed.",
                error=str(error)
            )