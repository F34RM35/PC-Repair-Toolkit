from datetime import datetime

from .repair import (
    RepairAction,
    RepairResult,
    RepairStatus,
)


class RepairManager:

    def __init__(self):
        self.actions = []

    def register(self, action: RepairAction):
        self.actions.append(action)

    def list_actions(self):
        return self.actions

    def run(self, action: RepairAction):

        started = datetime.now()

        result = RepairResult(
            name=action.name,
            status=RepairStatus.RUNNING,
            risk=action.risk,
            started_at=started.isoformat(
                timespec="seconds"
            ),
        )

        try:

            data = action.function()

            completed = datetime.now()

            result.status = RepairStatus.COMPLETED
            result.message = (
                "Repair action completed successfully."
            )
            result.data = data
            result.completed_at = completed.isoformat(
                timespec="seconds"
            )
            result.duration_seconds = round(
                (
                    completed - started
                ).total_seconds(),
                2
            )

            return result

        except Exception as error:

            completed = datetime.now()

            result.status = RepairStatus.FAILED
            result.message = (
                "Repair action failed."
            )
            result.error = str(error)
            result.completed_at = completed.isoformat(
                timespec="seconds"
            )
            result.duration_seconds = round(
                (
                    completed - started
                ).total_seconds(),
                2
            )

            return result