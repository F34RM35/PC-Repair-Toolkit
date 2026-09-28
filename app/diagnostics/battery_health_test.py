from app.diagnostics.battery import get_battery_info
from app.diagnostics.battery_health import analyze_battery


def main():
    batteries = get_battery_info()

    print()
    print("=" * 60)
    print("BATTERY HEALTH ANALYSIS")
    print("=" * 60)

    if not batteries:
        print("No battery information detected.")
        return

    for battery in batteries:
        result = analyze_battery(battery)

        print()
        print(f"Battery: {result.name}")
        print(f"Status:  {result.status.value}")
        print(f"Message: {result.message}")

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()