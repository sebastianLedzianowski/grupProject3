from flask import Flask

from src.menu.console_interface.abstractmethod.main_menu import MainMenu
from src.menu.console_interface.console_interface_main import console_interface_main

app = Flask(__name__)

@app.route('/')
def main():
    console_interface = MainMenu()
    console_interface_main(console_interface)

if __name__ == "__main__":
    main()