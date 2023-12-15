from uiLayer.display_ui import Display_UI
import os
from uiLayer import constants

class PM_UI:
    
    def __init__(self):
        pass

    def menu_output(self):
        os.system("cls")
        mainmenu = Display_UI()
        mainmenu.print_header()
        print("-Planning Manager Menu-".center(140))
        print()
        print(" " * 40, "[1] Register New Plane".ljust(100))
        print(" " * 40, "[2] List Planes".ljust(100))
        print(" " * 40, "[3] Plan New Voyage".ljust(100))
        print(" " * 40, "[4] See Saved Voyages".ljust(100))
        print()
        print()
        mainmenu.print_footer()
        print(constants.NAVBAR.center(140))
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
            menu.print_choose_type_of_plane_register()
            command = input("Enter your command: ")
            if command == "1":
                """De Havilland Canada DHC-8-200"""
                command2 = ""
                while command2 != "b":
                    os.system("cls")
                    menu.print_plane_register(name, plane_type, manufacturer, seats)
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        pot_name = input("Enter the planes name: ")
                        if pot_name.lower() == "b":
                            pass
                        else:
                            name = pot_name
                    elif command2.lower() == "s":
                        """Senda gögn"""
                        command2 = "b"
                        command = "b"
            elif command == "2":
                """De Havilland Canada DHC-8-400"""
                command2 = ""
                while command2 != "b":
                    os.system("cls")
                    menu.print_plane_register(name, plane_type, manufacturer, seats)
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        pot_name = input("Enter the planes name: ")
                        if pot_name.lower() == "b":
                            pass
                        else:
                            name = pot_name
                    elif command2.lower() == "s":
                        """Senda gögn"""
                        command2 = "b"
                        command = "b"
            elif command == "3":
                """Fokker 100"""
                command2 = ""
                while command2 != "b":
                    os.system("cls")
                    menu.print_plane_register(name, plane_type, manufacturer, seats)
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        pot_name = input("Enter the planes name: ")
                        if pot_name.lower() == "b":
                            pass
                        else:
                            name = pot_name
                    elif command2.lower() == "s":
                        """Senda gögn"""
                        command2 = "b"
                        command = "b"
            elif command == "4":
                """Bombardier CRJ700"""
                command2 = ""
                while command2 != "b":
                    os.system("cls")
                    menu.print_plane_register(name, plane_type, manufacturer, seats)
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        pot_name = input("Enter the planes name: ")
                        if pot_name.lower() == "b":
                            pass
                        else:
                            name = pot_name
                    elif command2.lower() == "s":
                        """Senda gögn"""
                        command2 = "b"
                        command = "b"
            elif command == "5":
                """Sukhoi Superjet 100"""
                command2 = ""
                while command2 != "b":
                    os.system("cls")
                    menu.print_plane_register(name, plane_type, manufacturer, seats)
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        pot_name = input("Enter the planes name: ")
                        if pot_name.lower() == "b":
                            pass
                        else:
                            name = pot_name
                    elif command2.lower() == "s":
                        """Senda gögn"""
                        command2 = "b"
                        command = "b"

    def list_of_airplanes(self):
        command = ""
        while command != "b":
            os.system("cls")
            menu = Display_UI()
            menu.print_choose_type_of_plane_list()
            command = input("Enter your command: ")
            if command == "1":
                """De Havilland Canada DHC-8-200"""
                command2 = ""
                while command2.lower() != "b":
                    os.system("cls")
                    menu.print_list_of_planes("De Havilland Canada DHC-8-200")
                    command2 = input("Enter your command: ")
            elif command == "2":
                """De Havilland Canada DHC-8-400"""
                command2 = ""
                while command2.lower() != "b":
                    os.system("cls")
                    menu.print_list_of_planes("De Havilland Canada DHC-8-400")
                    command2 = input("Enter your command: ")
            elif command == "3":
                """Fokker 100"""
                command2 = ""
                while command2.lower() != "b":
                    os.system("cls")
                    menu.print_list_of_planes("Fokker 100")
                    command2 = input("Enter your command: ")
            elif command == "4":
                """Bombardier CRJ700"""
                command2 = ""
                while command2.lower() != "b":
                    os.system("cls")
                    menu.print_list_of_planes("Bombardier CRJ700")
                    command2 = input("Enter your command: ")
            elif command == "5":
                """Sukhoi Superjet 100"""
                command2 = ""
                while command2.lower() != "b":
                    os.system("cls")
                    menu.print_list_of_planes("Sukhoi Superjet 100")
                    command2 = input("Enter your command: ")

    
    def register_voyage(self):
        command = ""
        departure = "ICELAND"
        destination = ""
        date1 = ""
        date2 = ""
        time1 = ""
        time2 = ""
        plane = ""
        while command != "b":
            os.system("cls")
            menu = Display_UI()
            menu.print_register_new_voyage(departure, destination, date1, date2, time1, time2, plane)
            command = input("Enter your command: ")
            if command == "1":
                command2 = ""
                while command2 != "b":
                    os.system("cls")
                    menu.print_select_destination()
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        destination = "NUUK"
                        command2 = "b"
                    elif command2 == "2":
                        destination = "KULUSUK"
                        command2 = "b"
                    elif command2 == "3":
                        destination = "TORSHAVN"
                        command2 = "b"
                    elif command2 == "4":
                        destination = "TINGWALL"
                        command2 = "b"
                    elif command2 == "5":
                        destination = "LONGYEARBYEN"
                        command2 = "b"
            elif command == "2":
                pot_date1 = input("Enter the Departure date: ")
                if pot_date1.lower() == "b":
                    pass
                else:
                    date1 = pot_date1
            elif command == "3":
                pot_date2 = input("Enter the Departure date: ")
                if pot_date2.lower() == "b":
                    pass
                else:
                    date2 = pot_date2
            elif command == "4":
                pass
            elif command == "5":
                pot_time1 = input("Enter the Departure time: ")
                if pot_time1.lower() == "b":
                    pass
                else:
                    time1 = pot_time1
            elif command == "6":
                pot_time2 = input("Enter the Departure time: ")
                if pot_time2.lower() == "b":
                    pass
                else:
                    time2 = pot_time2

    #def edit_voyage_info(self):
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
            print(constants.NAVBAR.center(140))
            menu.print_footer()
            command = input("Enter your command: ")

    def copy_voyage_info(self):
        pass

    



