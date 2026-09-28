from app.core.machine import get_machine_info


def main():
    machine = get_machine_info()

    print()
    print("=" * 60)
    print("MACHINE INFORMATION TEST")
    print("=" * 60)

    for key, value in machine.items():
        print()
        print(f"{key.upper()}")
        print("-" * 60)
        print(value)

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()