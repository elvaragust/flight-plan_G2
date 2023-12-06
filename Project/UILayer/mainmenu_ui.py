from display_ui import Display_UI
from pm_ui import PM_UI
from sm_ui import SM_UI
from s_ui import S_UI

class MainMenu_UI:
    
    def __init__(self):
        print("inside UI")

    def menu_output(self):
        print("Main Menu")
        print("1. Planning Manager")
        print("2. Staff Manager")
        print("3. Staff")
        print("q. quit")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "1":
                """Planning Manager"""
                menu = PM_UI()
                menu.input_prompt()
            elif command == "2":
                """Staff Manager"""
                menu = SM_UI()
                menu.input_prompt()
            elif command == "3":
                """Staff"""
                menu = S_UI()
                menu.input_prompt()
            elif command == "q":
                print("See you later!")
                break
            else:
                print("Invalid command!")