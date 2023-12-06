from UILayer.display_ui import Display_UI
from UILayer.pm_ui import PM_UI
from UILayer.sm_ui import SM_UI
from UILayer.s_ui import S_UI

class MainMenu:
    
    def __init__(self):
        pass

    def menu_output(self):
        display = Display_UI()
        display.print_display()

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "1":
                """Planning Manager"""
                menu = PM_UI()
                menu.input_prompt()
            elif command == "2":
                """Staff Manager"""
                menu = SM_UI()
                menu.input_prompt()
            elif command == "3":
                """Staff"""
                menu = S_UI()
                menu.input_prompt()
            elif command == "q":
                print("See you later!")
                break
            else:
                print("Invalid command!")