from app.diagnostics.drive_health import get_drive_health


def main():
    drives = get_drive_health()

    print()
    print("=" * 60)
    print("RAW DRIVE HEALTH INFORMATION")
    print("=" * 60)

    if not drives:
        print("No drive health information detected.")
        return

    if isinstance(drives, dict):
        for key, value in drives.items():
            print(f"{key:25}: {value}")

    else:
        for index, drive in enumerate(drives, start=1):
            print()
            print(f"DRIVE {index}")
            print("-" * 60)

            if isinstance(drive, dict):
                for key, value in drive.items():
                    print(f"{key:25}: {value}")
            else:
                print(drive)

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()