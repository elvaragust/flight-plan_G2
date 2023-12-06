from display_ui import Display_UI

class SM_UI:
    
    def __init__(self):
        pass

    def menu_output(self):
        mainmenu = Display_UI()
        mainmenu.print_header()
        print("-Planning Manager Menu-".center(140))
        print()
        print(" " * 40, "1. Register New Employee".ljust(100))
        print(" " * 40, "2. Change Employee Info".ljust(100))
        print(" " * 40, "3. List Employees".ljust(100))
        print(" " * 40, "4. Create Schedule".ljust(100))
        print(" " * 40, "5. Edit Schedule".ljust(100))
        print()
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
            elif command == "2":
                """Change Employee Info"""
            elif command == "3":
                """List Employees"""
            elif command == "4":
                """Create Schedule"""
            elif command == "5":
                """Edit schedule"""
            elif command == "b":
                print("Goin backwards")
                break
            else:
                print("Invalid command!")

    def register_employee(self):
        pass
    
    def create_schedules(self):
        pass

    def see_schedules(self):
        pass

    def edit_schedules(self):
        pass

    def copy_info(self):
        pass

    def delete_schedules(self):
        pass

    def list_employees(self):
        pass

    def change_employee_info(self):
        pass
