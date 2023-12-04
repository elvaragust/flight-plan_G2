class MainMenu:
    
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
                """Planning Manager"""
            elif command == "2":
                """Staff Manager"""
            elif command == "3":
                """Staff"""
            elif command == "q":
                print("See you later!")
                break
            else:
                print("Invalid command!")