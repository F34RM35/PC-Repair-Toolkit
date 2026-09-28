from app.core.repair import (
    RepairAction,
    RepairRisk,
)

from app.core.repair_manager import (
    RepairManager,
)

from app.core.repairs import (
    analyze_temp_files,
)


def main():

    print("=" * 60)
    print("             REPAIR ACTION TEST")
    print("=" * 60)

    action = RepairAction(
        name="Temporary File Analysis",
        description=(
            "Analyze Windows temporary files "
            "without deleting anything."
        ),
        risk=RepairRisk.READ_ONLY,
        function=analyze_temp_files,
    )

    manager = RepairManager()

    manager.register(action)

    print()
    print("AVAILABLE REPAIR")
    print("-" * 60)

    print(f"Name: {action.name}")
    print(f"Risk: {action.risk.value}")
    print(f"Description: {action.description}")

    print()
    print("Running analysis...")

    result = manager.run(action)

    print()
    print("RESULT")
    print("-" * 60)

    print(f"Status: {result.status.value}")
    print(f"Message: {result.message}")

    if result.data:

        print()
        print(f"Directory: {result.data['directory']}")
        print(f"Files:     {result.data['file_count']}")
        print(f"Size MB:   {result.data['total_mb']}")

    if result.error:
        print(f"Error: {result.error}")

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()