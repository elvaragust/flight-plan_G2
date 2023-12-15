import constants

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
        print("-Register New Employee-".center(140))
        print()
        print("[1]".rjust(50), "Name".ljust(20), name.ljust(70))
        print("[2]".rjust(50), "Rank".ljust(20), rank.ljust(70))
        print("[3]".rjust(50), "Email".ljust(20), email.ljust(70))
        print("[4]".rjust(50), "SSN".ljust(20), ssn.ljust(70))
        print("[5]".rjust(50), "Phone".ljust(20), phone.ljust(70))
        print("[6]".rjust(50), "Landline".ljust(20), landline.ljust(70))
        print("[7]".rjust(50), "License".ljust(20), license.ljust(70))
        print("[8]".rjust(50), "Home Address".ljust(20), home_address.ljust(70))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        boarder.print_footer()
        print(constants.NAVBAR2.center(140))
        boarder.print_footer()

    def print_edit_staff_information_management(self, name="", rank="" , email="", ssn="", phone="", landline="", license="", home_address=""):
        boarder = Display_UI()
        boarder.print_header()
        print("-Edit Employees Information-".center(140))
        print()
        print(" ".rjust(50), "Name".ljust(20), name.ljust(70))
        print("[1]".rjust(50), "Rank".ljust(20), rank.ljust(70))
        print("[2]".rjust(50), "Email".ljust(20), email.ljust(70))
        print(" ".rjust(50), "SSN".ljust(20), ssn.ljust(70))
        print("[3]".rjust(50), "Phone".ljust(20), phone.ljust(70))
        print("[4]".rjust(50), "Landline".ljust(20), landline.ljust(70))
        print("[5]".rjust(50), "License".ljust(20), license.ljust(70))
        print("[6]".rjust(50), "Home Address".ljust(20), home_address.ljust(70))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        boarder.print_footer()
        print(constants.NAVBAR2.center(140))
        boarder.print_footer()

    def print_choose_rank(self):
        boarder = Display_UI()
        boarder.print_header()
        print("-Choose A Rank-".center(140))
        print()
        print("[1]".rjust(55), " Pilot".ljust(85))
        print("[2]".rjust(55), " Flight Attendant".ljust(85))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    def print_edit_staff_information_staff(self, name="", rank="" , email="", ssn="", phone="", landline="", license="", home_address=""):
        boarder = Display_UI()
        boarder.print_header()
        print("-Edit Your Information-".center(140))
        print()
        print(" ".rjust(50), "Name".ljust(20), name.ljust(70))
        print(" ".rjust(50), "Rank".ljust(20), rank.ljust(70))
        print("[1]".rjust(50), "Email".ljust(20), email.ljust(70))
        print(" ".rjust(50), "SSN".ljust(20), ssn.ljust(70))
        print("[2]".rjust(50), "Phone".ljust(20), phone.ljust(70))
        print("[3]".rjust(50), "Landline".ljust(20), landline.ljust(70))
        print(" ".rjust(50), "License".ljust(20), license.ljust(70))
        print("[4]".rjust(50), "Home Address".ljust(20), home_address.ljust(70))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        boarder.print_footer()
        print(constants.NAVBAR2.center(140))
        boarder.print_footer()

    def print_find_employee(self, name="", rank="" , email="", ssn="", phone="", landline="", license="", home_address=""):
        boarder = Display_UI()
        boarder.print_header()
        print("-Employee Information-".center(140))
        print()
        print(" ".rjust(50), "Name".ljust(20), name.ljust(70))
        print(" ".rjust(50), "Rank".ljust(20), rank.ljust(70))
        print(" ".rjust(50), "Email".ljust(20), email.ljust(70))
        print(" ".rjust(50), "SSN".ljust(20), ssn.ljust(70))
        print(" ".rjust(50), "Phone".ljust(20), phone.ljust(70))
        print(" ".rjust(50), "Landline".ljust(20), landline.ljust(70))
        print(" ".rjust(50), "License".ljust(20), license.ljust(70))
        print(" ".rjust(50), "Home Address".ljust(20), home_address.ljust(70))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        boarder.print_footer()
        print(constants.NAVBAR2.center(140))
        boarder.print_footer()

    def print_plane_register(self, name="", type="", manufacturer="", seats=""):
        boarder = Display_UI()
        boarder.print_header()
        print("-Register New Plane-".center(140))
        print()
        print("[1]".rjust(50), "Name".ljust(20), name.ljust(70))
        print(" ".rjust(50), "Type".ljust(20), type.ljust(70))
        print(" ".rjust(50), "Manufacturer".ljust(20), manufacturer.ljust(70))
        print(" ".rjust(50), "Total Seats".ljust(20), seats.ljust(70))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        boarder.print_footer()
        print(constants.NAVBAR2.center(140))
        boarder.print_footer()

    def print_choose_type_of_plane_register(self):
        boarder = Display_UI()
        boarder.print_header()
        print("-Choose The Type Of Plane You Want To Register-".center(140))
        print()
        print("[1]".rjust(50), constants.PLANE1.ljust(90))
        print("[2]".rjust(50), constants.PLANE2.ljust(90))
        print("[3]".rjust(50), constants.PLANE3.ljust(90))
        print("[4]".rjust(50), constants.PLANE4.ljust(90))
        print("[5]".rjust(50), constants.PLANE5.ljust(90))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    def print_choose_license(self):
        boarder = Display_UI()
        boarder.print_header()
        print("-Choose A License-".center(140))
        print()
        print("[1]".rjust(50), constants.PLANE1.ljust(90))
        print("[2]".rjust(50), constants.PLANE2.ljust(90))
        print("[3]".rjust(50), constants.PLANE3.ljust(90))
        print("[4]".rjust(50), constants.PLANE4.ljust(90))
        print("[5]".rjust(50), constants.PLANE5.ljust(90))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    def print_choose_type_of_plane_list(self):
        boarder = Display_UI()
        boarder.print_header()
        print("-Choose The Type Of Plane You Want To List-".center(140))
        print()
        print("[1]".rjust(50), constants.PLANE1.ljust(90))
        print("[2]".rjust(50), constants.PLANE2.ljust(90))
        print("[3]".rjust(50), constants.PLANE3.ljust(90))
        print("[4]".rjust(50), constants.PLANE4.ljust(90))
        print("[5]".rjust(50), constants.PLANE5.ljust(90))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()


    def print_register_new_voyage(self, departure="", destination="", date1="", date2="", time1="", time2="", plane=""):
        boarder = Display_UI()
        boarder.print_header()
        print("-Register New Voyage-".center(140))
        print()
        print("From Iceland".center(70), "To Iceland".center(70))
        print()
        print(" ".rjust(15), " Departing From: ".ljust(20), departure.ljust(35)," ".rjust(15), "Departing From: ".ljust(20), destination.ljust(35))
        print("[1]".rjust(15), " Arriving In: ".ljust(20), destination.ljust(35)," ".rjust(15), "Arriving In: ".ljust(20), departure.ljust(35))
        print("[2]".rjust(15), " Date Departure: ".ljust(20), date1.ljust(35),"[3] ".rjust(15), "Date Departure: ".ljust(20), date2.ljust(35))
        print()
        print(f"[4] Choose Available Plane: {plane}".center(140))
        print()
        print("[5]".rjust(15), " Time Departing: ".ljust(20), time1.ljust(35),"[6] ".rjust(15), "Time Departing: ".ljust(20), time2.ljust(35))
        print(" ".rjust(15), " Date Arrival: ".ljust(20), date1.ljust(35)," ".rjust(15), "Date Arrival: ".ljust(20), date2.ljust(35))
        print(" ".rjust(15), " Time Arriving In: ".ljust(20), time1.ljust(35)," ".rjust(15), "Time Arriving In: ".ljust(20), time2.ljust(35))
        print()
        print()
        print()
        print()
        boarder.print_footer()
        print(constants.NAVBAR2.center(140))
        boarder.print_footer()

    def print_select_destination(self):
        boarder = Display_UI()
        boarder.print_header()
        print("-Select the Voyage's Destination-".center(140))
        print()
        print("[1] NUUK".center(140))
        print("[2] KULUSUK".center(140))
        print("[3] TORSHAVN".center(140))
        print("[4] TINGWALL".center(140))
        print("[5] LONGYEARBYEN".center(140))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    
    def print_select_crew(self, captain="", pilot="", cfa="", flight_attendant="", departure="", destination="", date1="", date2="", time1="", time2=""):
        boarder = Display_UI()
        boarder.print_header()
        print("-Register Crew On Voyage-".center(140))
        print()
        print("-From Iceland-".center(70), "-To Iceland-".center(70))
        print(" ".rjust(15), " Departing From: ".ljust(20), departure.ljust(35)," ".center(15), "Departing From: ".ljust(20), destination.ljust(35))
        print(" ".rjust(15), " Arriving In: ".ljust(20), destination.ljust(35)," ".center(15), "Arriving In: ".ljust(20), departure.ljust(35))
        print(" ".rjust(15), " Date Departure: ".ljust(20), date1.ljust(35)," ".center(15), "Date Departure: ".ljust(20), date2.ljust(35))
        print(" ".rjust(15), " Time Departing: ".ljust(20), time1.ljust(35)," ".center(15), "Time Departing: ".ljust(20), time2.ljust(35))
        print(" ".rjust(15), " Date Arrival: ".ljust(20), date1.ljust(35)," ".center(15), "Date Arrival: ".ljust(20), date2.ljust(35))
        print(" ".rjust(15), " Time Arriving In: ".ljust(20), "time1".ljust(35)," ".center(15), "Time Arriving In: ".ljust(20), "time2".ljust(35))
        print()
        print("-Staff-".center(140))
        print()
        print("[1]".rjust(55), " * Captain: ".ljust(20), captain.ljust(65))
        print("[2]".rjust(55), " * Pilot: ".ljust(20), pilot.ljust(65))
        print("[3]".rjust(55), " * CFA: ".ljust(20), cfa.ljust(65))
        print("[4]".rjust(55), "   Flight Attendant:".ljust(20), flight_attendant.ljust(65))
        print()
        boarder.print_footer()
        print(constants.NAVBAR2.center(140))
        boarder.print_footer()


    def print_list_of_employees(self, rank=""):
        """Dict{List}: SSN: NAME, RANK, """
        boarder = Display_UI()
        boarder.print_header()
        blabla = {1606982929: ["Gutti", "Flugþjónn", "5812345", "guttifreyr@hotmail.com"], 1512682323: ["Jónas", "Farþegi", "7741234", "jonashallgrims@gmail.is"]}
        print(f"-List of {rank}-".center(140))
        print(constants.DASH * 140)
        print("Name".center(34),"|", "SSN".center(20), "|", "Rank".center(19), "|", "Phone Number".center(20), "|", "Email".center(34))
        print(constants.DASH * 140)
        for key, value in blabla.items():
            if value[1] == rank:
                print(value[0].center(34),"|", f"{key}".center(20), "|", value[1].center(19), "|", value[2].center(20), "|", value[3].center(34))
            elif rank == "":
                print(value[0].center(34),"|", f"{key}".center(20), "|", value[1].center(19), "|", value[2].center(20), "|", value[3].center(34))
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    def print_choose_type_of_employee(self):
        boarder = Display_UI()
        boarder.print_header()
        print("-Choose Type Of Employee To List-".center(140))
        print()
        print(" ".ljust(55), "[1] All Employees".ljust(85))
        print(" ".ljust(55), "[2] Pilots".ljust(85))
        print(" ".ljust(55), "[3] Flight Attendants".ljust(85))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    def print_list_of_planes(self):
        """Dict{List}: NAME: TYPE, MANUFACTURER, SEATS"""
        boarder = Display_UI()
        boarder.print_header()
        print(f"-Airplane List-".center(140))
        print(constants.DASH * 140)
        #for key, value in plane_type.items():
         #   pass
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()
        
    def print_list_of_saved_voyages(self):
        boarder = Display_UI()
        boarder.print_header()
        print("-Saved Voyages-".center(140))
        print(constants.DASH * 140)
        # for key, value in voyages.items()
            #
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    def print_see_schedule(self):
        boarder = Display_UI()
        boarder.print_header()
        print("-Schedule-".center(140))
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    def print_existing_voyages(self):
        boarder = Display_UI()
        boarder.print_header()
        voyages_dict = {"1": ["Iceland", "Nuuk", "14/11/21", "17:00", "14/11/21", "21:00"], "2": ["Iceland", "Tingwall", "16/11/21", "14:00", "16/11/21", "17:00"]}
        print("-Existing Voyages-".center(140))
        print(constants.DASH * 140)
        print(" ".center(5), "|", "Departing From".center(20), "|", "Arriving To".center(20), "|", f"Time From Iceland".center(30), "|", "Time From Destination".center(30))
        print(constants.DASH * 140)
        counter = 1
        for key, value in voyages_dict.items():
            print(f"[{counter}]".center(5), "|", value[0].center(20), "|", value[1].center(20), "|", f"{value[2]}--{value[3]}".center(30), "|", f"{value[4]}--{value[5]}".center(30))
            counter += 1
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()