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
        print(" " * 40, "[1] Register New Employee".ljust(100))
        print(" " * 40, "[2] Change Employee Info".ljust(100))
        print(" " * 40, "[3] List Employees".ljust(100))
        print(" " * 40, "[4] Select Crew On Voyages".ljust(100))
        print(" " * 40, "[5] See Schedule".ljust(100))
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
                """Register New Employee"""
                choice = SM_UI()
                choice.register_employee()
            elif command == "2":
                """Change Employee Info"""
                ssn = input("Enter the Social Security number of an employee: ")
                #if ssn in employee_dict:
                 #   pass
                choice = SM_UI()
                choice.change_employee_info()
            elif command == "3":
                """List Employees"""
                choice = SM_UI()
                choice.list_employees()
            elif command == "4":
                """Select Crew on Voyages"""
                choice = SM_UI()
                choice.select_crew_on_voyages()
            elif command == "5":
                """See Schedule"""
                choice = SM_UI()
                choice.see_schedules()
            elif command == "b":
                print("Going backwards")
                break
            else:
                print("Invalid command!")

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
        while command != "b":
            os.system("cls")
            menu = Display_UI()
            menu.print_staff_register(name, rank, email, ssn, phone, landline, plane_license, home_address)
            command = input("Enter your command: ")
            if command == "1":
                pot_name = input("Enter the Name: ")
                if pot_name.lower() == "b":
                    pass
                else:
                    name = pot_name
            elif command == "2":
                pot_rank = input("Enter the Rank: ")
                if pot_rank.lower() == "b":
                    pass
                else:
                    rank = pot_rank
            elif command == "3":
                pot_email = input("Enter the Email: ")
                if pot_email.lower() == "b":
                    pass
                else:
                    email = pot_email
            elif command == "4":
                pot_ssn = input("Enter the Social Security Number: ")
                if pot_ssn.lower() == "b":
                    pass
                else:
                    ssn = pot_ssn
            elif command == "5":
                pot_phone = input("Enter the phone number: ")
                if pot_phone.lower() == "b":
                    pass
                else:
                    phone = pot_phone
            elif command == "6":
                pot_landline = input("Enter the landline number: ")
                if pot_landline.lower() == "b":
                    pass
                else:
                    landline = pot_landline
            elif command == "7":
                pot_plane_license = input("Enter the plane license: ")
                if pot_plane_license.lower() == "b":
                    pass
                else:
                    plane_license = pot_plane_license
            elif command == "8":
                pot_home_address = input("Enter the home address: ")
                if pot_home_address.lower() == "b":
                    pass
                else:
                    home_address = pot_home_address

    
    def change_employee_info(self):
        command = ""
        while command != "b":
            os.system("cls")
            menu = Display_UI()
            menu.print_edit_staff_information_management()
            command = input("Enter your command: ")
            if command == "1":
                pot_rank = input("Enter the Employee's rank: ")
                if pot_rank.lower() == "b":
                    pass
                else:
                    rank = pot_rank
            elif command == "2":
                pot_email = input("Enter the Employee's email: ")
                if pot_email.lower() == "b":
                    pass
                else:
                    email = pot_email
            elif command == "3":
                pot_phone = input("Enter the Employee's phone number: ")
                if pot_phone.lower() == "b":
                    pass
                else:
                    phone = pot_phone
            elif command == "4":
                pot_landline = input("Enter the Employee's landline number: ")
                if pot_landline.lower() == "b":
                    pass
                else:
                    landline = pot_landline
            elif command == "5":
                pot_plane_license = input("Enter the Employee's plane license: ")
                if pot_plane_license.lower() == "b":
                    pass
                else:
                    plane_license = pot_plane_license
            elif command == "6":
                pot_home_address = input("Enter the Employee's home address: ")
                if pot_home_address.lower() == "b":
                    pass
                else:
                    home_address = pot_home_address
            
    def list_employees(self):
        command = ""
        while command != "b":
            os.system("cls")
            menu = Display_UI()
            menu.print_list_of_employees()
            command = input("Enter your command: ")

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
        while command != "b":
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

    

    
