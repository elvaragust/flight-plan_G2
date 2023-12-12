class Display_UI:

    def __init__(self):
        pass

    def print_header(self):
        print("=" * 140)
        print(" " * 51, "_   __        _   __   ___     _", " " * 55)
        print(" " * 50, "/ | / /____ _ / | / /  /   |   (_)_____", " " * 49)
        print(" " * 19, "__|__", " " * 23, "/  |/ // __ `//  |/ /  / /| |  / // ___/", " " * 24, "__|__", " " * 19)
        print(" " * 13, "-o--o--(_)--o--o-", " " * 16, "/ /|  // /_/ // /|  /  / ___ | / // /", " " * 22, "-o--o--(_)--o--o-", " " * 14)
        print(" " * 47, "/_/ |_/ \__,_//_/ |_/  /_/  |_|/_//_/", " ")
        print()
        print("I" * 140)
        print()
        print()

    def print_footer(self):
        print("-" * 140)


    def print_staff_register(self, name="", rank="" , email="", ssn="", phone="", landline="", license="", home_address=""):
        boarder = Display_UI()
        boarder.print_header()
        print("Name".rjust(60), name.ljust(80))
        print("Rank".rjust(60), rank.ljust(80))
        print("Email".rjust(60), email.ljust(80))
        print("SSN".rjust(60), ssn.ljust(80))
        print("Phone".rjust(60), phone.ljust(80))
        print("Landline".rjust(60), landline.ljust(80))
        print("License".rjust(60), license.ljust(80))
        print("Home Adress".rjust(60), home_address.ljust(80))
        print()
        boarder.print_footer()
        

