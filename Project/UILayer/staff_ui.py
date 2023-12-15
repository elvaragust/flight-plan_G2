from uiLayer.display_ui import Display_UI
import os
from uiLayer import constants

class S_UI:
    
    def __init__(self):
        pass

    def menu_output(self):
        os.system("cls")
        mainmenu = Display_UI()
        mainmenu.print_header()
        print("-Staff Menu-".center(140))
        print()
        print(" ".ljust(55), "[1] See Shift Plan".ljust(85))
        print(" ".ljust(55), "[2] Change Personal Information".ljust(85))
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
        print()
        mainmenu.print_footer()
        print(constants.NAVBAR.center(140))
        mainmenu.print_footer()

    def input_prompt(self, ssn):
        menu_command = ""
        command = ""
        while command.lower() != "b" and command.lower() != "back":
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "1":
                """See Shift Plan"""
                choice = S_UI()
                menu_command = choice.see_schedule(ssn)
            elif command == "2":
                """Change Personal Information"""
                choice = S_UI()
                menu_command = choice.change_basic_info()
            elif command.lower() == "b" or command.lower() == "back":
                print("Goin backwards")
                return "b"
            elif command.lower() == "h" or command.lower() == "home":
                return "b"
            else:
                print("Invalid command!")
            if menu_command == "b":
                return "b"

    def change_basic_info(self):
        command = ""
        while command != "b" and command != "back":
            os.system("cls")
            menu = Display_UI()
            menu.print_edit_staff_information_staff()
            command = input("Enter your command: ")
            if command == "1":
                pot_email = input("Enter your Email: ")
                if pot_email.lower() == "b" or pot_email.lower() == "back":
                    pass
                else:
                    email = pot_email
            elif command == "2":
                pot_phone = input("Enter your phone number: ")
                if pot_phone.lower() == "b" or pot_phone.lower() == "back":
                    pass
                else:
                    phone = pot_phone
            elif command == "3":
                pot_landline = input("Enter your landline number: ")
                if pot_landline.lower() == "b" or pot_landline.lower() == "back":
                    pass
                else:
                    landline = pot_landline
            elif command == "4":
                pot_home_address = input("Enter your home address: ")
                if pot_home_address.lower() == "b" or pot_home_address.lower() == "back":
                    pass
                else:
                    home_address = pot_home_address.capitalize()
            elif command.lower() == "h" or command.lower() == "home":
                return "b"
        

    def see_schedule(self, ssn):
        command = ""
        while command.lower() != "b" and command.lower() != "back":
            os.system("cls")
            menu = Display_UI()
            menu.print_see_schedule(ssn)
            command = input("Enter your command: ")
            if command.lower() == "h" or command.lower() == "home":
                return "b"

   

