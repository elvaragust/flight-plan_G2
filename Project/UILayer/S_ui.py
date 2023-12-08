from display_ui import Display_UI

class S_UI:
    
    def __init__(self):
        pass

    def menu_output(self):
        mainmenu = Display_UI()
        mainmenu.print_header()
        print("-Planning Manager Menu-".center(140))
        print()
        print(" " * 40, "1. See Shift Plan".ljust(100))
        print(" " * 40, "2. Change Personal Information".ljust(100))
        print(" " * 40, "3. Register Leave/Vacation".ljust(100))
        print()
        print()
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
                """See Shift Plan"""
                choice = S_UI()
                choice.see_schedule()
            elif command == "2":
                """Change Personal Information"""
                choice = S_UI()
                choice.change_basic_info()
            elif command == "3":
                """Register Leave/Vacation"""
                choice = S_UI()
                choice.request_time_off()
            elif command == "b":
                print("Goin backwards")
                break
            else:
                print("Invalid command!")

    def change_basic_info(self):
        command = ""
        while command != "b":
            menu = Display_UI()
            menu.print_header()
            print()
            menu.print_footer()
            print("[B]ack    [N]ext    [P]rev".center(140))
            command = input("Enter your command: ")
        

    def see_schedule(self):
        command = ""
        while command != "b":
            menu = Display_UI()
            menu.print_header()
            print()
            menu.print_footer()
            print("[B]ack    [N]ext    [P]rev".center(140))
            command = input("Enter your command: ")

    def request_time_off(self):
        command = ""
        while command != "b":
            menu = Display_UI()
            menu.print_header()
            print()
            menu.print_footer()
            print("[B]ack    [N]ext    [P]rev".center(140))
            command = input("Enter your command: ")


