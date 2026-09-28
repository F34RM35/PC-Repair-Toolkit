from app.diagnostics.storage import get_storage_info


def main():
    storage = get_storage_info()

    print()
    print("=" * 60)
    print("RAW STORAGE INFORMATION")
    print("=" * 60)

    if not storage:
        print("No storage information detected.")
        return

    if isinstance(storage, dict):
        for key, value in storage.items():
            print(f"{key:25}: {value}")

    else:
        for index, drive in enumerate(storage, start=1):
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