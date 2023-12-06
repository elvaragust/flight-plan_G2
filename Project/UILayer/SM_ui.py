from display_ui import Display_UI

class SM_UI:
    
    def __init__(self):
        pass

    def menu_output(self):
        print("Staff Manager Menu")
        print("1. Employees")
        print("2. Schedule")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "1":
                """Employees"""
            elif command == "2":
                """Schedule"""
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
