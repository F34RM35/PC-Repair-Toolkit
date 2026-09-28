from app.diagnostics.storage import get_storage_info
from app.diagnostics.storage_health import analyze_storage


def main():
    drives = get_storage_info()

    print()
    print("=" * 60)
    print("STORAGE HEALTH ANALYSIS")
    print("=" * 60)

    if not drives:
        print("No storage information detected.")
        return

    for drive in drives:
        result = analyze_storage(drive)

        print()
        print(f"Drive:   {result.name}")
        print(f"Status:  {result.status.value}")
        print(f"Message: {result.message}")

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()