from display_ui import Display_UI
import os

class PM_UI:
    
    def __init__(self):
        pass

    def menu_output(self):
        os.system("cls")
        mainmenu = Display_UI()
        mainmenu.print_header()
        print("-Planning Manager Menu-".center(140))
        print()
        print(" " * 40, "1. Register New Plane".ljust(100))
        print(" " * 40, "2. List Planes".ljust(100))
        print(" " * 40, "3. Plan New Voyage".ljust(100))
        print(" " * 40, "4. Edit Voyage".ljust(100))
        print(" " * 40, "5. See Saved Voyages".ljust(100))
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
                choice = PM_UI()
                choice.register_airplane()
            elif command == "2":
                """List Planes"""
                choice = PM_UI()
                choice.list_of_airplanes()
            elif command == "3":
                """Plan New Voyage"""
                choice = PM_UI()
                choice.register_voyage()
            elif command == "4":
                """Edit Voyage"""
                choice = PM_UI()
                choice.edit_plane_info()
            elif command == "5":
                """See Saved Voyages"""
                choice = PM_UI()
                choice.list_saved_voyages()
            elif command == "b":
                print("Goin backwards")
                break
            else:
                print("Invalid command!")


    def register_airplane(self):
        command = ""
        name = ""
        plane_type = ""
        manufacturer = ""
        seats = ""
        while command != "b":
            os.system("cls")
            menu = Display_UI()
            menu.print_choose_type_of_plane()
            command = input("Enter your command: ")
            if command == "1":
                """De Havilland Canada DHC-8-200"""
            elif command == "2":
                """De Havilland Canada DHC-8-400"""
            elif command == "3":
                """Fokker 100"""
            elif command == "4":
                """Bombardier CRJ700"""
            elif command == "5":
                """Sukhoi Superjet 100"""

    def list_of_airplanes(self):
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
    
    def register_voyage(self):
        command = ""
        while command != "b":
            os.system("cls")
            menu = Display_UI()
            menu.print_register_new_voyage()
            command = input("Enter your command: ")

    def edit_voyage_info(self):
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

    def save_voyage_info(self):
        pass

    def list_saved_voyages(self):
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

    def copy_voyage_info(self):
        pass

    



