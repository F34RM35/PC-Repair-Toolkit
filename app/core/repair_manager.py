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

        try:

            result = action.function()

            return RepairResult(
                name=action.name,
                status=RepairStatus.COMPLETED,
                message="Repair action completed successfully.",
                data=result,
            )

        except Exception as error:

            return RepairResult(
                name=action.name,
                status=RepairStatus.FAILED,
                message="Repair action failed.",
                error=str(error),
            )