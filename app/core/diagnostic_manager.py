from app.core.result import DiagnosticResult, DiagnosticStatus

from app.diagnostics.system import get_system_info
from app.diagnostics.cpu import get_cpu_info
from app.diagnostics.memory import get_memory_info
from app.diagnostics.storage import get_storage_info
from app.diagnostics.drive_health import get_drive_health
from app.diagnostics.battery import get_battery_info
from app.diagnostics.battery_health import analyze_battery


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

        results["battery"] = self._run_battery()

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

    def _run_battery(self):
        try:
            batteries = get_battery_info()

            if not batteries:
                return DiagnosticResult(
                    name="Battery",
                    status=DiagnosticStatus.UNKNOWN,
                    data=None,
                    message="No battery information detected."
                )

            battery_results = []

            for battery in batteries:
                result = analyze_battery(battery)
                battery_results.append(result)

            statuses = [
                result.status
                for result in battery_results
            ]

            if DiagnosticStatus.CRITICAL in statuses:
                overall_status = DiagnosticStatus.CRITICAL

            elif DiagnosticStatus.WARNING in statuses:
                overall_status = DiagnosticStatus.WARNING

            elif DiagnosticStatus.UNKNOWN in statuses:
                overall_status = DiagnosticStatus.UNKNOWN

            else:
                overall_status = DiagnosticStatus.PASS

            return DiagnosticResult(
                name="Battery",
                status=overall_status,
                data=battery_results,
                message="Battery health analysis completed."
            )

        except Exception as error:
            return DiagnosticResult(
                name="Battery",
                status=DiagnosticStatus.UNKNOWN,
                data=None,
                message="Battery analysis could not be completed.",
                error=str(error)
            )