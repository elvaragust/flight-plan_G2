from display_ui import Display_UI
import os
import constants

class S_UI:
    
    def __init__(self):
        pass

    def menu_output(self):
        os.system("cls")
        mainmenu = Display_UI()
        mainmenu.print_header()
        print("-Staff Menu-".center(140))
        print()
        print(" " * 40, "[1] See Shift Plan".ljust(100))
        print(" " * 40, "[2] Change Personal Information".ljust(100))
        print(" " * 40, "[3] Register Leave/Vacation".ljust(100))
        print()
        print()
        print()
        print()
        print()
        mainmenu.print_footer()
        print(constants.NAVBAR.center(140))
        mainmenu.print_footer()

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "1":
                """See Shift Plan"""
                choice = S_UI()
                choice.see_schedule()
            elif command == "2":
                """Change Personal Information"""
                choice = S_UI()
                choice.change_basic_info()
            elif command == "3":
                """Register Leave/Vacation"""
                choice = S_UI()
                choice.request_time_off()
            elif command == "b":
                print("Goin backwards")
                return "b"
            else:
                print("Invalid command!")

    def change_basic_info(self):
        command = ""
        while command != "b":
            os.system("cls")
            menu = Display_UI()
            menu.print_edit_staff_information_staff()
            command = input("Enter your command: ")
            if command == "1":
                pot_email = input("Enter your Email: ")
                if pot_email.lower() == "b":
                    pass
                else:
                    email = pot_email
            elif command == "2":
                pot_phone = input("Enter your phone number: ")
                if pot_phone.lower() == "b":
                    pass
                else:
                    phone = pot_phone
            elif command == "3":
                pot_landline = input("Enter your landline number: ")
                if pot_landline.lower() == "b":
                    pass
                else:
                    landline = pot_landline
            elif command == "4":
                pot_home_address = input("Enter your home address: ")
                if pot_home_address.lower() == "b":
                    pass
                else:
                    home_address = pot_home_address
        

    def see_schedule(self):
        command = ""
        while command != "b":
            os.system("cls")
            menu = Display_UI()
            menu.print_header()
            print()
            menu.print_footer()
            print(constants.NAVBAR.center(140))
            menu.print_footer()
            command = input("Enter your command: ")

    def request_time_off(self):
        command = ""
        while command != "b":
            os.system("cls")
            menu = Display_UI()
            menu.print_header()
            print()
            menu.print_footer()
            print(constants.NAVBAR.center(140))
            menu.print_footer()
            command = input("Enter your command: ")


