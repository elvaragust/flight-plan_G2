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
            elif command == "2":
                """Change Personal Information"""
            elif command == "3":
                """Register Leave/Vacation"""
            elif command == "b":
                print("Goin backwards")
                break
            else:
                print("Invalid command!")

    def change_basic_info(self):
        pass

    def see_schedule(self):
        pass

    def request_time_off(self):
        pass


