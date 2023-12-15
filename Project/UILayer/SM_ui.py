from display_ui import Display_UI
import os
import constants

class SM_UI:
    
    def __init__(self):
        pass

    def menu_output(self):
        os.system("cls")
        mainmenu = Display_UI()
        mainmenu.print_header()
        print("-Staff Manager Menu-".center(140))
        print()
        print(" ".ljust(55), "[1] Register New Employee".ljust(85))
        print(" ".ljust(55), "[2] Change Employee Info".ljust(85))
        print(" ".ljust(55), "[3] List Employees".ljust(85))
        print(" ".ljust(55), "[4] Find Employee".ljust(85))
        print(" ".ljust(55), "[5] Select Crew On Voyages".ljust(85))
        print(" ".ljust(55), "[6] See Schedule".ljust(85))
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

    def input_prompt(self):
        menu_command = ""
        command = ""
        while command.lower() != "b" and command.lower() != "back":
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "1":
                """Register New Employee"""
                choice = SM_UI()
                menu_command = choice.register_employee()

            elif command == "2":
                """Change Employee Info"""
                ssn = input("Enter the Social Security number of an employee: ")
                #if ssn in employee_dict:
                 #   pass
                choice = SM_UI()
                menu_command = choice.change_employee_info()

            elif command == "3":
                """List Employees"""
                choice = SM_UI()
                menu_command = choice.list_employees()

            elif command == "4":
                """Find Employee"""
                ssn = input("Enter the Social Security number of an employee: ")
                #if ssn in employee_dict:
                 #   pass
                choice = SM_UI()
                menu_command = choice.find_employee()

            elif command == "4":
                """Select Crew on Voyages"""
                choice = SM_UI()
                menu_command = choice.select_crew_on_voyages()

            elif command == "5":
                """See Schedule"""
                choice = SM_UI()
                menu_command = choice.see_schedules()

            elif command.lower() == "b" or command.lower() == "back":
                print("Going backwards")

            elif command.lower() == "h" or command.lower() == "home":
                command = "b"

            else:
                print("Invalid command!")

            if menu_command == "b":
                command = "b"

    def register_employee(self):
        command = ""
        name = ""
        rank = ""
        email = ""
        ssn = ""
        phone = ""
        landline = ""
        plane_license = ""
        home_address = ""
        while command.lower() != "b" and command.lower() != "back":
            os.system("cls")
            menu = Display_UI()
            menu.print_staff_register(name, rank, email, ssn, phone, landline, plane_license, home_address)
            command = input("Enter your command: ")
            if command == "1":
                pot_name = input("Enter the Name: ")
                if pot_name.lower() == "b" or pot_name.lower() == "back":
                    pass
                else:
                    name = pot_name.capitalize()
            elif command == "2":
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_choose_rank()
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        rank = "Pilot"
                        command2 = "b"
                    elif command2 == "2":
                        rank = "Flight Attendant"
                        command2 = "b"
                    elif command2.lower() == "h" or command2.lower() == "home":
                        return "b"
            elif command == "3":
                pot_email = input("Enter the Email: ")
                if pot_email.lower() == "b" or pot_email.lower() == "back":
                    pass
                else:
                    email = pot_email
            elif command == "4":
                pot_ssn = input("Enter the Social Security Number: ")
                if pot_ssn.lower() == "b" or pot_ssn.lower() == "back":
                    pass
                else:
                    ssn = pot_ssn
            elif command == "5":
                pot_phone = input("Enter the phone number: ")
                if pot_phone.lower() == "b" or pot_phone.lower() == "back":
                    pass
                else:
                    phone = pot_phone
            elif command == "6":
                pot_landline = input("Enter the landline number: ")
                if pot_landline.lower() == "b" or pot_landline.lower() == "back":
                    pass
                else:
                    landline = pot_landline
            elif command == "7":
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_choose_license()
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        plane_license = constants.PLANE1
                        command2 = "b"
                    elif command2 == "2":
                        plane_license = constants.PLANE2
                        command2 = "b"
                    elif command2 == "3":
                        plane_license = constants.PLANE3
                        command2 = "b"
                    elif command2 == "4":
                        plane_license = constants.PLANE4
                        command2 = "b"
                    elif command2 == "5":
                        plane_license = constants.PLANE5
                        command2 = "b"
                    elif command2.lower() == "h" or command2.lower() == "home":
                        return "b"
            elif command == "8":
                pot_home_address = input("Enter the home address: ")
                if pot_home_address.lower() == "b" or pot_home_address.lower() == "back":
                    pass
                else:
                    home_address = pot_home_address.capitalize()
            elif command.lower() == "h" or command.lower() == "home":
                return "b"

    
    def change_employee_info(self):
        command = ""
        while command.lower() != "b" and command.lower() != "back":
            os.system("cls")
            menu = Display_UI()
            menu.print_edit_staff_information_management()
            command = input("Enter your command: ")
            if command == "1":
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_choose_rank()
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        rank = "Pilot"
                        command2 = "b"
                    elif command2 == "2":
                        rank = "Flight Attendant"
                        command2 = "b"
                    elif command2.lower() == "h" or command2.lower() == "home":
                        return "b"
            elif command == "2":
                pot_email = input("Enter the Employee's email: ")
                if pot_email.lower() == "b" or pot_email.lower() == "back":
                    pass
                else:
                    email = pot_email
            elif command == "3":
                pot_phone = input("Enter the Employee's phone number: ")
                if pot_phone.lower() == "b" or pot_phone.lower() == "back":
                    pass
                else:
                    phone = pot_phone
            elif command == "4":
                pot_landline = input("Enter the Employee's landline number: ")
                if pot_landline.lower() == "b" or pot_landline.lower() == "back":
                    pass
                else:
                    landline = pot_landline
            elif command == "5":
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_choose_license()
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        plane_license = constants.PLANE1
                        command2 = "b"
                    elif command2 == "2":
                        plane_license = constants.PLANE2
                        command2 = "b"
                    elif command2 == "3":
                        plane_license = constants.PLANE3
                        command2 = "b"
                    elif command2 == "4":
                        plane_license = constants.PLANE4
                        command2 = "b"
                    elif command2 == "5":
                        plane_license = constants.PLANE5
                        command2 = "b"
                    elif command2.lower() == "h" or command2.lower() == "home":
                        return "b"
            elif command == "6":
                pot_home_address = input("Enter the Employee's home address: ")
                if pot_home_address.lower() == "b" or pot_home_address.lower() == "back":
                    pass
                else:
                    home_address = pot_home_address.capitalize()
            elif command.lower() == "h" or command.lower() == "home":
                return "b"
            
    def find_employee(self):
        command = ""
        while command.lower() != "b" and command.lower() != "back":
            os.system("cls")
            menu = Display_UI()
            menu.print_find_employee()
            command = input("Enter your command: ")
            if command.lower() == "h" or command.lower() == "home":
                return "b"
            
    def list_employees(self):
        command = ""
        while command.lower() != "b" and command.lower() != "back":
            os.system("cls")
            menu = Display_UI()
            menu.print_choose_type_of_employee()
            command = input("Enter your command: ")
            if command == "1":
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_list_of_employees()
                    command2 = input("Enter your command: ")
                    if command2.lower() == "h" or command2.lower() == "home":
                        return "b"
            elif command == "2":
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_list_of_employees("Flugþjónn")
                    command2 = input("Enter your command: ")
                    if command2.lower() == "h" or command2.lower() == "home":
                        return "b"
            elif command == "3":
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_list_of_employees("Farþegi")
                    command2 = input("Enter your command: ")
                    if command2.lower() == "h" or command2.lower() == "home":
                        return "b"
            elif command.lower() == "h" or command.lower() == "home":
                return "b"

    def select_crew_on_voyages(self):
        command = ""
        while command != "b":
            os.system("cls")
            menu = Display_UI()
            menu.print_select_crew()
            command = input("Enter your command: ")

    #def edit_crew_on_voyages(self):
     #   command = ""
      #  while command != "b":
       #     os.system("cls")
        #    menu = Display_UI()
         #   menu.print_header()
          #  print()
           # menu.print_footer()
            #print(constants.NAVBAR.center(140))
            #menu.print_footer()
            #command = input("Enter your command: ")

    def see_schedules(self):
        command = ""
        while command.lower() != "b" and command.lower() != "back":
            os.system("cls")
            menu = Display_UI()
            menu.print_header()
            print()
            menu.print_footer()
            print(constants.NAVBAR.center(140))
            menu.print_footer()
            command = input("Enter your command: ")

    def copy_info(self):
        pass

    def delete_schedules(self):
        pass

    

    
