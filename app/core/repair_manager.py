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

            return RepairResult(
                name=action.name,
                status=RepairStatus.FAILED,
                message="Repair action is not registered.",
                error=(
                    "The requested repair action "
                    "is not registered with this manager."
                ),
            )

        # ----------------------------------------------------
        # Safety enforcement
        # ----------------------------------------------------

        if action.risk != RepairRisk.READ_ONLY:

            if not confirmed:

                return RepairResult(
                    name=action.name,
                    status=RepairStatus.CANCELLED,
                    message=(
                        "Repair action requires "
                        "explicit confirmation."
                    ),
                )

        # ----------------------------------------------------
        # Execute repair
        # ----------------------------------------------------

        try:

            result = action.function()

            return RepairResult(
                name=action.name,
                status=RepairStatus.COMPLETED,
                message=(
                    "Repair action completed successfully."
                ),
                data=result,
            )

        except Exception as error:

            return RepairResult(
                name=action.name,
                status=RepairStatus.FAILED,
                message="Repair action failed.",
                error=str(error),
            )