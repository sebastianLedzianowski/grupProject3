from src.menu.console_interface.console_interface_main import console_interface_main
from src.menu.console_interface.abstractmethod.main_menu import MainMenu


def main():
    console_interface = MainMenu()
    console_interface_main(console_interface)

if __name__ == "__main__":
    main()