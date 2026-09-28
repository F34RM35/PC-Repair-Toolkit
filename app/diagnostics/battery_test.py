from app.diagnostics.battery import get_battery_info


def main():
    batteries = get_battery_info()

    print()
    print("=" * 60)
    print("RAW BATTERY INFORMATION")
    print("=" * 60)

    if not batteries:
        print("No battery information detected.")
        return

    for index, battery in enumerate(batteries, start=1):
        print()
        print(f"BATTERY {index}")
        print("-" * 60)

        for key, value in battery.items():
            print(f"{key:25}: {value}")


if __name__ == "__main__":
    main()