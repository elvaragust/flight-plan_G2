from display_ui import Display_UI
from pm_ui import PM_UI
from sm_ui import SM_UI
from s_ui import S_UI

class MainMenu_UI:
    
    def __init__(self):
        print("inside UI")

    def menu_output(self):
        mainmenu = Display_UI()
        mainmenu.print_header()
        print("-Main Menu-".center(140))
        print()
        print(" " * 40, "1. Planning Manager".ljust(100))
        print(" " * 40, "2. Staff Manager".ljust(100))
        print(" " * 40, "3. Staff".ljust(100))
        print()
        print()
        print()
        print()
        print()
        mainmenu.print_footer()
        print("[Q]uit".center(140))
        mainmenu.print_footer()
        

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
                password = input("Enter your social security number: ")
                """Check if ssn is valid"""
                menu = S_UI()
                menu.input_prompt()
            elif command == "q":
                print("See you later!")
                break
            else:
                print("Invalid command!")