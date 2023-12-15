from uiLayer.display_ui import Display_UI
import os
from uiLayer import constants
from uiLayer.validation_ui import ValidationL

class SM_UI:
    
    def __init__(self):
        self.validation = ValidationL()

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
                menu_command = choice.change_employee_info(ssn)

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

            elif command == "5":
                """Select Crew on Voyages"""
                choice = SM_UI()
                menu_command = choice.select_crew_on_voyages()

            elif command == "6":
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
        
        value_list = ["","","","","","",""]
        employee_create_dict = {}
        
        while command.lower() != "b" and command.lower() != "back":
            os.system("cls")
            menu = Display_UI()
            menu.print_staff_register(name, rank, email, ssn, phone, landline, plane_license, home_address)
            command = input("Enter your command: ")
            if command == "1":
                while True:
                    pot_name = input("Enter the Name: ")
                    if pot_name.lower() == "b" or pot_name.lower() == "back":
                        break
                    elif pot_name.lower() == "h" or pot_name.lower() == "home":
                        return "b"
                    else:
                        try:
                            self.validation.validate_employee_name(pot_name)
                            name = pot_name.capitalize()
                            value_list[0] = pot_name.capitalize()
                            break
                        except ValueError:
                            print("Invalid Name")
                            pass

           
          
            elif command == "2":
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_choose_rank()
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        rank = "Pilot"
                        value_list[1] = rank
                        command2 = "b"
                    elif command2 == "2":
                        rank = "Flight Attendant"
                        value_list[1] = rank
                        command2 = "b"
                    elif command2.lower() == "h" or command2.lower() == "home":
                        return "b"
        

            elif command == "3":
                while True:
                    pot_email = input("Enter the Email: ")
                    if pot_email.lower() == "b" or pot_email.lower() == "back":
                        break
                    elif pot_email.lower() == "h" or pot_email.lower() == "home":
                        return "b"
                    else:
                        try:
                            self.validation.validate_email(pot_email)
                            email = pot_email
                            value_list[2] = pot_email
                            break
                        except ValueError:
                            print("Invalid Email")
                            pass


                #pot_email = input("Enter the Email: ")

                #if pot_email.lower() == "b" or pot_email.lower() == "back":
                 #   pass
                #else:
                 #   if not self.validation.validate_email(pot_email):
                  #      pass
                   # else:
                    #    email = pot_email
                     #   value_list[2] = pot_email
                        
            elif command == "4":
                while True:
                    pot_ssn = input("Enter the Social Security Number: ")
                    if pot_ssn.lower() == "b" or pot_ssn.lower() == "back":
                        break
                    elif pot_ssn.lower() == "h" or pot_ssn.lower() == "home":
                        return "b"
                    else:
                        try:
                            self.validation.validate_employee_ssn(pot_ssn)
                            ssn = pot_ssn
                            break
                        except ValueError:
                            print("Invalid Social Security Number")
                            pass

                #pot_ssn = input("Enter the Social Security Number: ")
                #if pot_ssn.lower() == "b" or pot_ssn.lower() == "back":
                 #   pass
                #else:
                 #   if not self.validation.validate_employee_ssn(pot_ssn):
                  #      pass
                   # else:
                    #    ssn = pot_ssn
                     #   employee_create_dict[ssn] = value_list
                    
            elif command == "5":
                while True:
                    pot_phone = input("Enter the Phone Number: ")
                    if pot_phone.lower() == "b" or pot_phone.lower() == "back":
                        break
                    elif pot_phone.lower() == "h" or pot_phone.lower() == "home":
                        return "b"
                    else:
                        try:
                            self.validation.validate_phone(pot_phone)
                            phone = pot_phone
                            value_list[3] = pot_phone
                            break
                        except ValueError:
                            print("Invalid Phone Number")
                            pass

                #pot_phone = input("Enter the Phone number: ")

                #if pot_phone.lower() == "b" or pot_phone.lower() == "back":
                 #   pass
                #else:
                 #   if not self.validation.validate_phone(pot_phone):
                  #      pass
                   # else:
                    #    phone = pot_phone
                     #   value_list[3] = pot_phone
                        
            elif command == "6":
                while True:
                    pot_landline = input("Enter the Landline Number: ")
                    if pot_landline.lower() == "b" or pot_landline.lower() == "back":
                        break
                    elif pot_landline.lower() == "h" or pot_landline.lower() == "home":
                        return "b"
                    else:
                        try:
                            self.validation.validate_employee_landline(pot_landline)
                            landline = pot_landline
                            value_list[4] = pot_landline
                            break
                        except ValueError:
                            print("Invalid Landline Number")
                            pass

                #pot_landline = input("Enter the Landline Number: ")

                #if pot_landline.lower() == "b" or pot_landline.lower() == "back":
                 #   pass
                #else:
                 #   if not self.validation.validate_employee_landline(pot_landline):
                  #      pass
                   # else:
                    #    landline = pot_landline
                     #   value_list[4] = pot_landline
                        
            elif command == "7":

                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_choose_license()
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        plane_license = constants.PLANE1
                        value_list[5] = plane_license
                        command2 = "b"
                    elif command2 == "2":
                        plane_license = constants.PLANE2
                        value_list[5] = plane_license
                        command2 = "b"
                    elif command2 == "3":
                        plane_license = constants.PLANE3
                        value_list[5] = plane_license
                        command2 = "b"
                    elif command2 == "4":
                        plane_license = constants.PLANE4
                        value_list[5] = plane_license
                        command2 = "b"
                    elif command2 == "5":
                        plane_license = constants.PLANE5
                        value_list[5] = plane_license
                        command2 = "b"
                    elif command2.lower() == "h" or command2.lower() == "home":
                        return "b"

            elif command == "8":
                while True:
                    pot_home_address = input("Enter the Home Address: ")
                    if pot_home_address.lower() == "b" or pot_home_address.lower() == "back":
                        break
                    elif pot_home_address.lower() == "h" or pot_home_address.lower() == "home":
                        return "b"
                    else:
                        try:
                            self.validation.validate_employee_address(pot_home_address)
                            home_address = pot_home_address.capitalize()
                            value_list[6] = pot_home_address.capitalize()
                            break
                        except ValueError:
                            print("Invalid Landline Number")
                            pass

                #pot_home_address = input("Enter the home address: ")
                #if pot_home_address.lower() == "b" or pot_home_address.lower() == "back":
                 #   pass
                #else:
                 #   home_address = pot_home_address.capitalize()
            elif command.lower() == "s" or command.lower() == "save":
                command = "b"
            elif command.lower() == "h" or command.lower() == "home":
                return "b"

    
    def change_employee_info(self, employee_ssn):
        command = ""
        name = ""
        rank = ""
        email = ""
        ssn = employee_ssn
        phone = ""
        landline = ""
        plane_license = ""
        home_address = ""
        
        value_list = ["","","","","","",""]
        employee_create_dict = {}

        while command.lower() != "b" and command.lower() != "back":
            os.system("cls")
            menu = Display_UI()
            menu.print_edit_staff_information_management(name, rank, email, ssn, phone, landline, plane_license, home_address)
            command = input("Enter your command: ")
            if command == "1":
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_choose_rank()
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        rank = "Pilot"
                        value_list[1] = rank
                        command2 = "b"
                    elif command2 == "2":
                        rank = "Flight Attendant"
                        value_list[1] = rank
                        command2 = "b"
                    elif command2.lower() == "h" or command2.lower() == "home":
                        return "b"
            elif command == "2":
                while True:
                    pot_email = input("Enter the Email: ")
                    if pot_email.lower() == "b" or pot_email.lower() == "back":
                        break
                    elif pot_email.lower() == "h" or pot_email.lower() == "home":
                        return "b"
                    else:
                        try:
                            self.validation.validate_email(pot_email)
                            email = pot_email
                            value_list[2] = pot_email
                            break
                        except ValueError:
                            print("Invalid Email")
                            pass
                
                #pot_email = input("Enter the Employee's email: ")
                #if pot_email.lower() == "b" or pot_email.lower() == "back":
                 #   pass
                #else:
                 #   email = pot_email
            elif command == "3":
                while True:
                    pot_phone = input("Enter the Phone Number: ")
                    if pot_phone.lower() == "b" or pot_phone.lower() == "back":
                        break
                    elif pot_phone.lower() == "h" or pot_phone.lower() == "home":
                        return "b"
                    else:
                        try:
                            self.validation.validate_phone(pot_phone)
                            phone = pot_phone
                            value_list[3] = pot_phone
                            break
                        except ValueError:
                            print("Invalid Phone Number")
                            pass

                #pot_phone = input("Enter the Employee's phone number: ")
                #if pot_phone.lower() == "b" or pot_phone.lower() == "back":
                 #   pass
                #else:
                 #   phone = pot_phone
            elif command == "4":
                while True:
                    pot_landline = input("Enter the Landline Number: ")
                    if pot_landline.lower() == "b" or pot_landline.lower() == "back":
                        break
                    elif pot_landline.lower() == "h" or pot_landline.lower() == "home":
                        return "b"
                    else:
                        try:
                            self.validation.validate_employee_landline(pot_landline)
                            landline = pot_landline
                            value_list[4] = pot_landline
                            break
                        except ValueError:
                            print("Invalid Landline Number")
                            pass

                #pot_landline = input("Enter the Employee's landline number: ")
                #if pot_landline.lower() == "b" or pot_landline.lower() == "back":
                 #   pass
                #else:
                 #   landline = pot_landline
            elif command == "5":
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_choose_license()
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        plane_license = constants.PLANE1
                        value_list[5] = plane_license
                        command2 = "b"
                    elif command2 == "2":
                        plane_license = constants.PLANE2
                        value_list[5] = plane_license
                        command2 = "b"
                    elif command2 == "3":
                        plane_license = constants.PLANE3
                        value_list[5] = plane_license
                        command2 = "b"
                    elif command2 == "4":
                        plane_license = constants.PLANE4
                        value_list[5] = plane_license
                        command2 = "b"
                    elif command2 == "5":
                        plane_license = constants.PLANE5
                        value_list[5] = plane_license
                        command2 = "b"
                    elif command2.lower() == "h" or command2.lower() == "home":
                        return "b"
            elif command == "6":
                while True:
                    pot_home_address = input("Enter the Home Address: ")
                    if pot_home_address.lower() == "b" or pot_home_address.lower() == "back":
                        break
                    elif pot_home_address.lower() == "h" or pot_home_address.lower() == "home":
                        return "b"
                    else:
                        try:
                            self.validation.validate_employee_address(pot_home_address)
                            home_address = pot_home_address.capitalize()
                            value_list[6] = pot_home_address.capitalize()
                            break
                        except ValueError:
                            print("Invalid Landline Number")
                            pass

                #pot_home_address = input("Enter the Employee's home address: ")
                #if pot_home_address.lower() == "b" or pot_home_address.lower() == "back":
                 #   pass
                #else:
                 #   home_address = pot_home_address.capitalize()
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
                    menu.print_list_of_employees("Pilot")
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
            elif command == "4":
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_list_of_employees_working("Yes")
                    command2 = input("Enter your command: ")
                    if command2.lower() == "h" or command2.lower() == "home":
                        return "b"
            elif command == "5":
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_list_of_employees_working("No")
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
            menu.print_existing_voyages()
            command = input("Enter your command: ")
            if command.lower() == "b" or command.lower() == "back":
                pass
            elif command.lower() == "h" or command.lower() == "home":
                return "b"
            else:
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_select_crew()
                    command2 = input("Enter your command: ")
                    if command2.lower() == "h" or command2.lower() == "home":
                        return "b"


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
            menu.print_see_schedule()
            command = input("Enter your command: ")

    def copy_info(self):
        pass

    def delete_schedules(self):
        pass

    

    
