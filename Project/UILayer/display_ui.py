from uiLayer import constants

class Display_UI:

    def __init__(self):
        pass

    def print_header(self):
        print(constants.EQUALS * 140)
        print(" " * 51, "_   __        _   __   ___     _", " " * 55)
        print(" " * 50, "/ | / /____ _ / | / /  /   |   (_)_____", " " * 49)
        print(" " * 19, "__|__", " " * 23, "/  |/ // __ `//  |/ /  / /| |  / // ___/", " " * 24, "__|__", " " * 19)
        print(" " * 13, "-o--o--(_)--o--o-", " " * 16, "/ /|  // /_/ // /|  /  / ___ | / // /", " " * 22, "-o--o--(_)--o--o-", " " * 14)
        print(" " * 47, "/_/ |_/ \__,_//_/ |_/  /_/  |_|/_//_/", " ")
        print()
        print(constants.ISYMBOL * 140)
        print()
        print()

    def print_footer(self):
        print(constants.DASH * 140)


    def print_staff_register(self, name="", rank="" , email="", ssn="", phone="", landline="", license="", home_address=""):
        boarder = Display_UI()
        boarder.print_header()
        print("Register New Employee".center(140))
        print()
        print("[1]".rjust(50), "Name".rjust(20), name.ljust(70))
        print("[2]".rjust(50), "Rank".rjust(20), rank.ljust(70))
        print("[3]".rjust(50), "Email".rjust(20), email.ljust(70))
        print("[4]".rjust(50), "SSN".rjust(20), ssn.ljust(70))
        print("[5]".rjust(50), "Phone".rjust(20), phone.ljust(70))
        print("[6]".rjust(50), "Landline".rjust(20), landline.ljust(70))
        print("[7]".rjust(50), "License".rjust(20), license.ljust(70))
        print("[8]".rjust(50), "Home Address".rjust(20), home_address.ljust(70))
        print()
        boarder.print_footer()
        print(constants.NAVBAR2.center(140))
        boarder.print_footer()

    def print_edit_staff_information_management(self, name="", rank="" , email="", ssn="", phone="", landline="", license="", home_address=""):
        boarder = Display_UI()
        boarder.print_header()
        print("Edit Employees Information".center(140))
        print()
        print(" ".rjust(50), "Name".rjust(20), name.ljust(70))
        print("[1]".rjust(50), "Rank".rjust(20), rank.ljust(70))
        print("[2]".rjust(50), "Email".rjust(20), email.ljust(70))
        print(" ".rjust(50), "SSN".rjust(20), ssn.ljust(70))
        print("[3]".rjust(50), "Phone".rjust(20), phone.ljust(70))
        print("[4]".rjust(50), "Landline".rjust(20), landline.ljust(70))
        print("[5]".rjust(50), "License".rjust(20), license.ljust(70))
        print("[6]".rjust(50), "Home Address".rjust(20), home_address.ljust(70))
        print()
        boarder.print_footer()
        print(constants.NAVBAR2.center(140))
        boarder.print_footer()

    def print_edit_staff_information_staff(self, name="", rank="" , email="", ssn="", phone="", landline="", license="", home_address=""):
        boarder = Display_UI()
        boarder.print_header()
        print("Edit Your Information".center(140))
        print()
        print(" ".rjust(50), "Name".rjust(20), name.ljust(70))
        print(" ".rjust(50), "Rank".rjust(20), rank.ljust(70))
        print("[1]".rjust(50), "Email".rjust(20), email.ljust(70))
        print(" ".rjust(50), "SSN".rjust(20), ssn.ljust(70))
        print("[2]".rjust(50), "Phone".rjust(20), phone.ljust(70))
        print("[3]".rjust(50), "Landline".rjust(20), landline.ljust(70))
        print(" ".rjust(50), "License".rjust(20), license.ljust(70))
        print("[4]".rjust(50), "Home Address".rjust(20), home_address.ljust(70))
        print()
        boarder.print_footer()
        print(constants.NAVBAR2.center(140))
        boarder.print_footer()


    def print_plane_register(self, name="", type="", manufacturer="", seats=""):
        boarder = Display_UI()
        boarder.print_header()
        print("Register New Plane".center(140))
        print()
        print("[1]".rjust(50), "Name".rjust(20), name.ljust(70))
        print(" ".rjust(50), "Type".rjust(20), type.ljust(70))
        print(" ".rjust(50), "Manufacturer".rjust(20), manufacturer.ljust(70))
        print(" ".rjust(50), "Total seats".rjust(20), seats.ljust(70))
        print()
        boarder.print_footer()
        print(constants.NAVBAR2.center(140))
        boarder.print_footer()

    def print_choose_type_of_plane_register(self):
        boarder = Display_UI()
        boarder.print_header()
        print("Choose The Type of Plane You Want To Register".center(140))
        print()
        print("[1]".rjust(50), constants.PLANE1.ljust(90))
        print("[2]".rjust(50), constants.PLANE2.ljust(90))
        print("[3]".rjust(50), constants.PLANE3.ljust(90))
        print("[4]".rjust(50), constants.PLANE4.ljust(90))
        print("[5]".rjust(50), constants.PLANE5.ljust(90))
        print()
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    def print_choose_type_of_plane_list(self):
        boarder = Display_UI()
        boarder.print_header()
        print("Choose The Type of Plane You Want To List".center(140))
        print()
        print("[1]".rjust(50), constants.PLANE1.ljust(90))
        print("[2]".rjust(50), constants.PLANE2.ljust(90))
        print("[3]".rjust(50), constants.PLANE3.ljust(90))
        print("[4]".rjust(50), constants.PLANE4.ljust(90))
        print("[5]".rjust(50), constants.PLANE5.ljust(90))
        print()
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()


    def print_register_new_voyage(self, departure="", destination="", date1="", date2="", time1="", time2="", plane=""):
        boarder = Display_UI()
        boarder.print_header()
        print("Register New Voyage".center(140))
        print()
        print("From Iceland".center(70), "To Iceland".center(70))
        print()
        print(" ".rjust(10), " Departing from: ".ljust(20), departure.ljust(30)," ".rjust(10), "Departing from: ".ljust(20), destination.ljust(50))
        print("[1]".rjust(10), " Arriving in: ".ljust(20), destination.ljust(30)," ".rjust(10), "Arriving in: ".ljust(20), departure.ljust(50))
        print("[2]".rjust(10), " Date Departure: ".ljust(20), date1.ljust(30),"[3] ".rjust(10), "Date Departure: ".ljust(20), date2.ljust(50))
        print()
        print(f"[4] Choose Available Plane: {plane}".center(140))
        print()
        print("[5]".rjust(10), " Time Departing: ".ljust(20), time1.ljust(30),"[6] ".rjust(10), "Time Departing: ".ljust(20), time2.ljust(50))
        print(" ".rjust(10), " Date Arrival: ".ljust(20), date1.ljust(30)," ".rjust(10), "Date Arrival: ".ljust(20), date2.ljust(50))
        print(" ".rjust(10), " Time Arriving In: ".ljust(20), time1.ljust(30)," ".rjust(10), "Time Arriving In: ".ljust(20), time2.ljust(50))
        print()
        boarder.print_footer()
        print(constants.NAVBAR2.center(140))
        boarder.print_footer()

    def print_select_destination(self):
        boarder = Display_UI()
        boarder.print_header()
        print("Select the Voyage's destination")
        print()
        print("[1] NUUK".center(140))
        print("[2] KULUSUK".center(140))
        print("[3] TORSHAVN".center(140))
        print("[4] TINGWALL".center(140))
        print("[5] LONGYEARBYEN".center(140))
        print()
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    
    def print_select_crew(self):
        boarder = Display_UI()
        boarder.print_header()
        print("Register Crew on Voyage".center(140))
        print()
        print(" ".rjust(10), " Departing from: ".ljust(20), "departure".ljust(40), "Departing from: ".ljust(20), "destination".ljust(50))
        print(" ".rjust(10), " Arriving in: ".ljust(20), "destination".ljust(40), "Arriving in: ".ljust(20), "departure".ljust(50))
        print(" ".rjust(10), " Date Departure: ".ljust(20), "date1".ljust(40), "Date Departure: ".ljust(20), "date2".ljust(50))
        print(" ".rjust(10), " Time Departing: ".ljust(20), "time1".ljust(40), "Time Departing: ".ljust(20), "time2".ljust(50))
        print(" ".rjust(10), " Date Arrival: ".ljust(20), "date1".ljust(40), "Date Arrival: ".ljust(20), "date2".ljust(50))
        print(" ".rjust(10), " Time Arriving In: ".ljust(20), "time1".ljust(40), "Time Arriving In: ".ljust(20), "time2".ljust(50))
        print()
        print("-Staff-".center(70), "-Staff-".center(70))
        print()
        print("[1]".rjust(10), " * Captain: ".ljust(20), "captain".ljust(40), "[6]".rjust(10), " * Captain: ".ljust(20), "captain".ljust(40))
        print("[2]".rjust(10), " * Pilot: ".ljust(20), "pilot".ljust(40), "[7]".rjust(10), " * Pilot: ".ljust(20), "pilot".ljust(40))
        print("[3]".rjust(10), " * CFA: ".ljust(20), "cfa".ljust(40), "[8]".rjust(10), " * CFA: ".ljust(20), "cfa".ljust(40))
        print("[4]".rjust(10), "   Flight Attendant:".ljust(19), "flight attendant".ljust(40), " [9]".rjust(10), "   Flight Attendant:".ljust(20), "flight attendant".ljust(40))
        print()
        boarder.print_footer()
        print(constants.NAVBAR2.center(140))
        boarder.print_footer()


    def print_list_of_employees(self):
        """Dict{List}: SSN: NAME, RANK, """
        boarder = Display_UI()
        boarder.print_header()
        blabla = {1606982929: ["Gutti", "Flugþjónn"], 1512682323: ["Jónas", "Farþegi"]}
        print("List of Employees".center(140))
        print(constants.DASH * 140)
        for key, value in blabla.items():
            print(value[0].ljust(25),"|", f"{key}".ljust(15), "|", value[1].rjust(15))
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    def print_list_of_planes(self, plane_type):
        """Dict{List}: NAME: TYPE, MANUFACTURER, SEATS"""
        boarder = Display_UI()
        boarder.print_header()
        print(f"List of {plane_type}".center(140))
        print(constants.DASH * 140)
        #for key, value in plane_type.items():
         #   pass
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()
        
    def print_list_of_saved_voyages(self):
        boarder = Display_UI()
        boarder.print_header()