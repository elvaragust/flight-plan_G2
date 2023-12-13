from display_ui import Display_UI
import os

class SM_UI:
    
    def __init__(self):
        pass

    def menu_output(self):
        os.system("cls")
        mainmenu = Display_UI()
        mainmenu.print_header()
        print("-Staff Manager Menu-".center(140))
        print()
        print(" " * 40, "1. Register New Employee".ljust(100))
        print(" " * 40, "2. Change Employee Info".ljust(100))
        print(" " * 40, "3. List Employees".ljust(100))
        print(" " * 40, "4. Select Crew On Voyages".ljust(100))
        print(" " * 40, "5. Edit Crew On Voyages".ljust(100))
        print(" " * 40, "6. See Schedule".ljust(100))
        print()
        print()
        mainmenu.print_footer()
        print("[B]ack".center(140))
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
                """Edit Crew On Voyages"""
                choice = SM_UI()
                choice.edit_crew_on_voyages()
            elif command == "6":
                """See Schedule"""
                choice = SM_UI()
                choice.see_schedules()
            elif command == "b":
                print("Goin backwards")
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
                name = input("Enter the Name: ")
            elif command == "2":
                rank = input("Enter the Rank: ")
            elif command == "3":
                email = input("Enter the Email: ")
            elif command == "4":
                ssn = input("Enter the Social Security Number: ")
            elif command == "5":
                phone = input("Enter the phone number: ")
            elif command == "6":
                landline = input("Enter the landline number: ")
            elif command == "7":
                plane_license = input("Enter the plane license: ")
            elif command == "8":
                home_address = input("Enter the home address: ")

    
    def change_employee_info(self):
        command = ""
        while command != "b":
            os.system("cls")
            menu = Display_UI()
            menu.print_header()
            print()
            menu.print_footer()
            print("[B]ack    [N]ext    [P]rev".center(140))
            menu.print_footer()
            command = input("Enter your command: ")

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

    def edit_crew_on_voyages(self):
        command = ""
        while command != "b":
            os.system("cls")
            menu = Display_UI()
            menu.print_header()
            print()
            menu.print_footer()
            print("[B]ack    [N]ext    [P]rev".center(140))
            menu.print_footer()
            command = input("Enter your command: ")

    def see_schedules(self):
        command = ""
        while command != "b":
            os.system("cls")
            menu = Display_UI()
            menu.print_header()
            print()
            menu.print_footer()
            print("[B]ack    [N]ext    [P]rev".center(140))
            menu.print_footer()
            command = input("Enter your command: ")

    def copy_info(self):
        pass

    def delete_schedules(self):
        pass

    

    
