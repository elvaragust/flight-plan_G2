from uiLayer.display_ui import Display_UI
from logicLayer.logic_ui_wrapper import Logic_Wrapper
from uiLayer.planning_manager_ui import PM_UI
from uiLayer.staff_manager_ui import SM_UI
from uiLayer.staff_ui import S_UI
import os


class MainMenu_UI:
    def __init__(self):
        self.logic_ui_wrapper = Logic_Wrapper()

    def menu_output(self):
        """Prints the main menu"""
        os.system("cls")
        mainmenu = Display_UI()
        mainmenu.print_header()
        print("-Main Menu-".center(140))
        print()
        print(" ".ljust(55), "[1] Planning Manager".ljust(85))
        print(" ".ljust(55), "[2] Staff Manager".ljust(85))
        print(" ".ljust(55), "[3] Staff".ljust(85))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        mainmenu.print_footer()
        print("[Q]uit".center(140))
        mainmenu.print_footer()
        

    def input_prompt(self):
        """Prompts the user for input and calls the appropriate functions"""
        command = ""
        while command.lower() != "q" and command.lower() != "quit":
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
                ssn = ""
                while ssn.lower() != "b":
                    ssn = input("Enter your social security number: ")
                    employee_info = self.logic_ui_wrapper.get_employee_info(ssn)
                    if employee_info:
                        menu = S_UI()
                        _ = menu.input_prompt(ssn)
                    else:
                        print("Invalid input, Number needs to be 10 digits.")

            elif command.lower() == "q" or command.lower() == "quit":
                pass
            else:
                print("Invalid command!")
        os.system("cls")
        print("See You Later!")