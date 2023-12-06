from display_ui import Display_UI

class PM_UI:
    
    def __init__(self):
        pass

    def menu_output(self):
        print("Planning Manager Menu")
        print("1. Voyage")
        print("2. Airplane")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ").lower()
            if command == "1":
                """Plan New Voyage"""
            elif command == "2":
                """Change/Delete Voyage"""
            elif command == "3":
                """Register New Plane"""
            elif command == "4":
                """Change Info on Plane"""
            elif command == "5":
                """List Planes"""
            elif command == "6":
                """See Saved Voyages"""
            elif command == "b":
                print("Goin backwards")
                break
            else:
                print("Invalid command!")

    def register_business_trip(self):
        pass

    def register_airplane(self):
        pass

    def save_business_trip(self):
        pass

    def copy_business_trip(self):
        pass

    def list_of_airplanes(self):
        pass



