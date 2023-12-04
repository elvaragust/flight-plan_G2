class SM_UI:
    
    def __init__(self):
        pass

    def menu_output(self):
        pass

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "1":
                """Register Employee"""
            elif command == "2":
                """Create Shift Plan"""
            elif command == "3":
                """See Shift Plan"""
            elif command == "4":
                """Edit/Delete Shift Plan"""
            elif command == "5":
                """List All Employees"""
            elif command == "6":
                """Change Employee Information"""
            elif command == "7":
                """Register/Edit Flight Information"""
            elif command == "b":
                print("Goin backwards")
                break
            else:
                print("Invalid command!")

    def register_employees(self):
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
