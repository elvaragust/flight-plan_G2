from display_ui import Display_UI

class PM_UI:
    
    def __init__(self):
        pass

    def menu_output(self):
        mainmenu = Display_UI()
        mainmenu.print_header()
        print("-Planning Manager Menu-".center(140))
        print()
        print(" " * 40, "1. Register New Plane".ljust(100))
        print(" " * 40, "2. Edit Plane Info".ljust(100))
        print(" " * 40, "3. List Planes".ljust(100))
        print(" " * 40, "4. Plan New Voyage".ljust(100))
        print(" " * 40, "5. Edit Voyage".ljust(100))
        print(" " * 40, "6. See Saved Voyages".ljust(100))
        print()
        print()
        mainmenu.print_footer()
        print("[B]ack".center(140))
        mainmenu.print_footer()

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ").lower()
            if command == "1":
                """Register New Plane"""
            elif command == "2":
                """Edit Plane Info"""
            elif command == "3":
                """List Planes"""
            elif command == "4":
                """Plan New Voyage"""
            elif command == "5":
                """Edit Voyage"""
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



