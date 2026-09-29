from datetime import datetime

from .repair import (
    RepairAction,
    RepairResult,
    RepairRisk,
    RepairStatus,
)


class RepairManager:

    def __init__(self):
        self.actions = []

    def register(
        self,
        action: RepairAction
    ):
        self.actions.append(action)

    def list_actions(self):
        return self.actions

    def run(
        self,
        action: RepairAction,
        confirmed: bool = False
    ):

        # ----------------------------------------------------
        # Validate action
        # ----------------------------------------------------

        if action not in self.actions:

            now = datetime.now().isoformat(
                timespec="seconds"
            )

            return RepairResult(
                name=action.name,
                status=RepairStatus.FAILED,
                message="Repair action is not registered.",
                error=(
                    "The requested repair action "
                    "is not registered with this manager."
                ),
                risk=action.risk,
                started_at=now,
                completed_at=now,
                duration_seconds=0.0,
            )

        # ----------------------------------------------------
        # Safety enforcement
        # ----------------------------------------------------

        if action.risk != RepairRisk.READ_ONLY:

            if not confirmed:

                now = datetime.now().isoformat(
                    timespec="seconds"
                )

                return RepairResult(
                    name=action.name,
                    status=RepairStatus.CANCELLED,
                    message=(
                        "Repair action requires "
                        "explicit confirmation."
                    ),
                    risk=action.risk,
                    started_at=now,
                    completed_at=now,
                    duration_seconds=0.0,
                )

        # ----------------------------------------------------
        # Start execution
        # ----------------------------------------------------

        started = datetime.now()

        started_at = started.isoformat(
            timespec="seconds"
        )

        try:

            result = action.function()

            completed = datetime.now()

            duration = (
                completed - started
            ).total_seconds()

            return RepairResult(
                name=action.name,
                status=RepairStatus.COMPLETED,
                message=(
                    "Repair action completed successfully."
                ),
                data=result,
                risk=action.risk,
                started_at=started_at,
                completed_at=completed.isoformat(
                    timespec="seconds"
                ),
                duration_seconds=round(
                    duration,
                    3
                ),
            )

        except Exception as error:

            completed = datetime.now()

            duration = (
                completed - started
            ).total_seconds()

            return RepairResult(
                name=action.name,
                status=RepairStatus.FAILED,
                message="Repair action failed.",
                error=str(error),
                risk=action.risk,
                started_at=started_at,
                completed_at=completed.isoformat(
                    timespec="seconds"
                ),
                duration_seconds=round(
                    duration,
                    3
                ),
            )