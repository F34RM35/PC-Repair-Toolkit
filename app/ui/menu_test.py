from app.ui.menu import (
    show_header,
    show_menu,
    get_choice
)


def main():

    show_header()
    show_menu()

    choice = get_choice()

    print()
    print(f"You selected: {choice}")


if __name__ == "__main__":
    main()