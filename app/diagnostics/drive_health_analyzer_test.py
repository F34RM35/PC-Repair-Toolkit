from app.diagnostics.drive_health import get_drive_health
from app.diagnostics.drive_health_analyzer import analyze_drive_health


def main():
    drives = get_drive_health()

    print()
    print("=" * 60)
    print("DRIVE HEALTH ANALYSIS")
    print("=" * 60)

    if not drives:
        print("No drive health information detected.")
        return

    for drive in drives:
        result = analyze_drive_health(drive)

        print()
        print(f"Drive:   {drive.get('name', 'Unknown')}")
        print(f"Status:  {result.status.value}")
        print(f"Message: {result.message}")

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()