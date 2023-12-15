from display_ui import Display_UI
import os
import constants

class PM_UI:
    
    def __init__(self):
        pass

    def menu_output(self):
        os.system("cls")
        mainmenu = Display_UI()
        mainmenu.print_header()
        print("-Planning Manager Menu-".center(140))
        print()
        print(" ".ljust(55), "[1] Register New Plane".ljust(85))
        print(" ".ljust(55), "[2] List Planes".ljust(85))
        print(" ".ljust(55), "[3] Plan New Voyage".ljust(85))
        print(" ".ljust(55), "[4] See Saved Voyages".ljust(85))
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
            command = input("Enter your command: ").lower()
            if command == "1":
                """Register New Plane"""
                choice = PM_UI()
                menu_command = choice.register_airplane()
            elif command == "2":
                """List Planes"""
                choice = PM_UI()
                menu_command = choice.list_of_airplanes()
            elif command == "3":
                """Plan New Voyage"""
                choice = PM_UI()
                menu_command = choice.register_voyage()
            elif command == "4":
                """See Saved Voyages"""
                choice = PM_UI()
                menu_command = choice.list_saved_voyages()
            elif command.lower() == "b" or command.lower() == "back" or command.lower() == "h" or command.lower() == "home":
                print("Goin backwards")
                break
            else:
                print("Invalid command!")
            if menu_command == "b":
                break
        


    def register_airplane(self):
        command = ""
        name = ""
        plane_type = ""
        manufacturer = ""
        seats = ""
        while command != "b" and command != "back":
            os.system("cls")
            menu = Display_UI()
            menu.print_choose_type_of_plane_register()
            command = input("Enter your command: ")
            if command == "1":
                """De Havilland Canada DHC-8-200"""
                command2 = ""
                while command2 != "b" and command2 != "back":
                    os.system("cls")
                    menu.print_plane_register(name, plane_type, manufacturer, seats)
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        pot_name = input("Enter the planes name: ")
                        if pot_name.lower() == "b" or pot_name.lower() == "back":
                            pass
                        else:
                            name = pot_name
                    elif command2.lower() == "s" or command2.lower() == "save":
                        """Senda gögn"""
                        command2 = "b"
                        command = "b"
                    elif command2.lower() == "h" or command2.lower() == "home":
                        return "b"
            elif command == "2":
                """De Havilland Canada DHC-8-400"""
                command2 = ""
                while command2 != "b" and command2 != "back":
                    os.system("cls")
                    menu.print_plane_register(name, plane_type, manufacturer, seats)
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        pot_name = input("Enter the planes name: ")
                        if pot_name.lower() == "b" or pot_name.lower() == "back":
                            pass
                        else:
                            name = pot_name
                    elif command2.lower() == "s" or command2.lower() == "save":
                        """Senda gögn"""
                        command2 = "b"
                        command = "b"
                    elif command2.lower() == "h" or command2.lower() == "home":
                        return "b"
            elif command == "3":
                """Fokker 100"""
                command2 = ""
                while command2 != "b" and command2 != "back":
                    os.system("cls")
                    menu.print_plane_register(name, plane_type, manufacturer, seats)
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        pot_name = input("Enter the planes name: ")
                        if pot_name.lower() == "b" or pot_name.lower() == "back":
                            pass
                        else:
                            name = pot_name
                    elif command2.lower() == "s" or command2.lower() == "save":
                        """Senda gögn"""
                        command2 = "b"
                        command = "b"
                    elif command2.lower() == "h" or command2.lower() == "home":
                        return "b"
            elif command == "4":
                """Bombardier CRJ700"""
                command2 = ""
                while command2 != "b" and command2 != "back":
                    os.system("cls")
                    menu.print_plane_register(name, plane_type, manufacturer, seats)
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        pot_name = input("Enter the planes name: ")
                        if pot_name.lower() == "b" or pot_name.lower() == "back":
                            pass
                        else:
                            name = pot_name
                    elif command2.lower() == "s" or command2.lower() == "save":
                        """Senda gögn"""
                        command2 = "b"
                        command = "b"
                    elif command2.lower() == "h" or command2.lower() == "home":
                        return "b"
            elif command == "5":
                """Sukhoi Superjet 100"""
                command2 = ""
                while command2 != "b" and command2 != "back":
                    os.system("cls")
                    menu.print_plane_register(name, plane_type, manufacturer, seats)
                    command2 = input("Enter your command: ")
                    if command2 == "1":
                        pot_name = input("Enter the planes name: ")
                        if pot_name.lower() == "b" or pot_name.lower() == "back":
                            pass
                        else:
                            name = pot_name
                    elif command2.lower() == "s" or command2.lower() == "save":
                        """Senda gögn"""
                        command2 = "b"
                        command = "b"
                    elif command2.lower() == "h" or command2.lower() == "home":
                        return "b"
            elif command.lower() == "h" or command.lower() == "home":
                return "b"

    def list_of_airplanes(self):
        command = ""
        while command != "b" and command != "back":
            os.system("cls")
            menu = Display_UI()
            menu.print_choose_type_of_plane_list()
            command = input("Enter your command: ")
            if command == "1":
                """De Havilland Canada DHC-8-200"""
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_list_of_planes("De Havilland Canada DHC-8-200")
                    command2 = input("Enter your command: ")
                    if command2 == "h" or command2 == "home":
                        return "b"
            elif command == "2":
                """De Havilland Canada DHC-8-400"""
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_list_of_planes("De Havilland Canada DHC-8-400")
                    command2 = input("Enter your command: ")
                    if command2 == "h" or command2 == "home":
                        return "b"
            elif command == "3":
                """Fokker 100"""
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_list_of_planes("Fokker 100")
                    command2 = input("Enter your command: ")
                    if command2 == "h" or command2 == "home":
                        return "b"
            elif command == "4":
                """Bombardier CRJ700"""
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_list_of_planes("Bombardier CRJ700")
                    command2 = input("Enter your command: ")
                    if command2 == "h" or command2 == "home":
                        return "b"
            elif command == "5":
                """Sukhoi Superjet 100"""
                command2 = ""
                while command2.lower() != "b" and command2.lower() != "back":
                    os.system("cls")
                    menu.print_list_of_planes("Sukhoi Superjet 100")
                    command2 = input("Enter your command: ")
                    if command2 == "h" or command2 == "home":
                        return "b"

    
    def register_voyage(self):
        command = ""
        departure = "ICELAND"
        destination = ""
        date1 = ""
        date2 = ""
        time1 = ""
        time2 = ""
        plane = ""
        while command != "b" and command != "back":
            os.system("cls")
            menu = Display_UI()
            menu.print_register_new_voyage(departure, destination, date1, date2, time1, time2, plane)
            command = input("Enter your command: ")
            if command == "1":
                command2 = ""
                while command2 != "b" and command2 != "back":
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
                    elif command2 == "h" or command2 == "home":
                        return "b"
            elif command == "2":
                pot_date1 = input("Enter the Departure date: ")
                if pot_date1.lower() == "b" or pot_date1.lower() == "back":
                    pass
                else:
                    date1 = pot_date1
            elif command == "3":
                pot_date2 = input("Enter the Departure date: ")
                if pot_date2.lower() == "b" or pot_date2.lower() == "back":
                    pass
                else:
                    date2 = pot_date2
            elif command == "4":
                pass
            elif command == "5":
                pot_time1 = input("Enter the Departure time: ")
                if pot_time1.lower() == "b" or pot_time1.lower() == "back":
                    pass
                else:
                    time1 = pot_time1
            elif command == "6":
                pot_time2 = input("Enter the Departure time: ")
                if pot_time2.lower() == "b" or pot_time2.lower() == "back":
                    pass
                else:
                    time2 = pot_time2
            elif command.lower() == "h" or command.lower() == "home":
                return "b"

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
        while command.lower() != "b" and command.lower() != "back":
            os.system("cls")
            menu = Display_UI()
            menu.print_list_of_saved_voyages()
            command = input("Enter your command: ")

    



