from uiLayer.display_ui import Display_UI
from uiLayer.pm_ui import PM_UI
from uiLayer.sm_ui import SM_UI
from uiLayer.s_ui import S_UI
import os


class MainMenu_UI:
    
    def __init__(self):
        print("inside UI")

    def menu_output(self):
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
                    employee_info = self.data_layer.logic_data_wrapper.get_employee_info(ssn)
                    if employee_info:
                        menu = S_UI()
                        ssn = menu.input_prompt()
                    else:
                        print("Invalid input, please enter a number with 9 to 10 digits.")
            elif command.lower() == "q" or command.lower() == "quit":
                pass
            else:
                print("Invalid command!")
        os.system("cls")
        print("See you Later!")