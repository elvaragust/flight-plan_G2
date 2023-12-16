from uiLayer import constants
from logicLayer.logic_ui_wrapper import Logic_Wrapper

class Display_UI:

    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def print_header(self):
        """Prints the header of the program"""
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
        """ Prints the footer of the program"""
        print(constants.DASH * 140)


    def print_staff_register(self, name="", rank="" , email="", ssn="", phone="", landline="", license="", home_address=""):
        """Prints the staff register when registering new staff"""
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
        """Prints the staff register when editing staff information for management"""
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
        """Prints the choose rank menu"""
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
        """prints the staff register when editing staff information for staff"""
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

    def print_find_employee(self, ssn):
        employee = self.logic_wrapper.get_employee_info(ssn)
        boarder = Display_UI()
        boarder.print_header()
        print("-Employee Information-".center(140))
        print()
        print(" ".rjust(50), "Name".ljust(20), employee['Name'].ljust(70))
        print(" ".rjust(50), "Rank".ljust(20), employee['Rank'].ljust(70))
        print(" ".rjust(50), "Email".ljust(20), employee['Email'].ljust(70))
        print(" ".rjust(50), "SSN".ljust(20), employee['SSN'].ljust(70))
        print(" ".rjust(50), "Phone".ljust(20), employee['PhoneNumber'].ljust(70))
        print(" ".rjust(50), "Landline".ljust(20), employee['Landline'].ljust(70))
        print(" ".rjust(50), "License".ljust(20), employee['licence'].ljust(70))
        print(" ".rjust(50), "Home Address".ljust(20), employee['Address'].ljust(70))
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
        """Prints the plane register when registering new plane"""
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
        """Prints the choose type of plane menu when registering new plane"""
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
        """Prints the choose license menu when registering new employee"""
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
        """Prints the choose type of plane menu when listing planes"""
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
        """Prints the register new voyage menuu"""
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
        """Prints the select destination menu"""
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
        """Prints the select crew menu"""
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


    def print_list_of_employees(self):
        """Prints the list of employees	"""
        """Dict{List}: SSN: NAME, RANK, """
        boarder = Display_UI()
        boarder.print_header()
        print(f"-List of Employees-".center(140))
        print(constants.DASH * 140)
        print("Name".center(34),"|", "SSN".center(20), "|", "Rank".center(19), "|", "Phone Number".center(20), "|", "Email".center(34))
        print(constants.DASH * 140)

        employees = self.logic_wrapper.list_all_employees()
        for employee in employees:
            print(employee['Name'].ljust(34),"|",employee['SSN'].center(20), "|", employee['Rank'].ljust(19), "|", employee['PhoneNumber'].center(20), "|", employee['Email'].ljust(34))

        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    
    def print_list_of_pilots(self):
        """Prints the list of pilots"""
        boarder = Display_UI()
        boarder.print_header()
        print(f"-List of Employees-".center(140))
        print(constants.DASH * 140)
        print("Name".center(34),"|", "SSN".center(20), "|", "Rank".center(19), "|", "Phone Number".center(20), "|", "Email".center(34))
        print(constants.DASH * 140)

        employees = self.logic_wrapper.list_all_employees()
        for employee in employees:
            if employee['Rank'] == "Pilot":
                print(employee['Name'].ljust(34),"|",employee['SSN'].ljust(20), "|", employee['Rank'].ljust(19), "|", employee['PhoneNumber'].ljust(20), "|", employee['Email'].ljust(34))

        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    def print_list_of_flight_attendant(self):
        """Prints the list of flight attendants"""
        boarder = Display_UI()
        boarder.print_header()
        print(f"-List of Employees-".center(140))
        print(constants.DASH * 140)
        print("Name".center(34),"|", "SSN".center(20), "|", "Rank".center(19), "|", "Phone Number".center(20), "|", "Email".center(34))
        print(constants.DASH * 140)

        employees = self.logic_wrapper.list_all_employees()
        for employee in employees:
            if employee['Rank'] == 'Flight Attendant':
                print(employee['Name'].ljust(34),"|",employee['SSN'].ljust(20), "|", employee['Rank'].ljust(19), "|", employee['PhoneNumber'].ljust(20), "|", employee['Email'].ljust(34))

        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()


    def print_choose_type_of_employee(self):
        """Prints the choose type of employees list menu"""
        boarder = Display_UI()
        boarder.print_header()
        print("-Choose Type Of Employee To List-".center(140))
        print()
        print(" ".ljust(55), "[1] All Employees".ljust(85))
        print(" ".ljust(55), "[2] Pilots".ljust(85))
        print(" ".ljust(55), "[3] Flight Attendants".ljust(85))
        print(" ".ljust(55), "[4] Employees who are working today")
        print(" ".ljust(55), "[5] Employees who are not working today")
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
        boarder = Display_UI()
        boarder.print_header()
        print(f"-List of Airplanes-".center(140))
        print(constants.DASH * 140)
        print("Airplane Name".center(34),"|", "Model".center(20), "|", "Manufacturer".center(19), "|", "Seats".center(20))
        print(constants.DASH * 140)

        planes = self.logic_wrapper.get_all_airplanes()
        for plane in planes:
            print(plane['AirplaneName'].ljust(34),"|",plane['Model'].center(20), "|", plane['Manufacturer'].ljust(19), "|", plane['Seats'].center(20))
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()
        
    def print_list_of_saved_voyages(self):
        """Prints the list of saved voyages"""
        boarder = Display_UI()
        boarder.print_header()
        print("-Saved Voyages-".center(140))
        print(constants.DASH * 140)
        print("Eitthvað")
        print(constants.DASH * 140)
        # for key, value in dict.items()
            #
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    """def print_see_schedule(self, ssn):
        boarder = Display_UI()
        boarder.print_header()
        print("-Schedule-".center(140))
        print()
        schedule = self.logic_wrapper.see_schedule_specific(ssn)
        print(schedule)
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()"""

    def print_see_schedule(self, ssn):
        """Prints the schedule of the employee"""
        boarder = Display_UI()
        boarder.print_header()
        print(f"-Schedule {ssn}-".center(140))
        print(constants.DASH * 140)
        print("Flight Number".center(12),"|", "Departure Date".center(17), "|", "Departure Time".center(17), "|", "Arrival Date".center(12), "|", "Arrival Time".center(13),  "|", "From Destination".center(14), "|", "To Destination".center(12), "|", "Airplane Name".center(12))
        print(constants.DASH * 140)

        schedule = self.logic_wrapper.see_schedule_specific(ssn)
        for sched in schedule:
            print(sched['FlightNumber'].center(13),"|",sched['DepartureDate'].center(17), "|", sched['DepartureTime'].center(17), "|", sched['ArrivalDate'].center(12), "|", sched['ArrivalTime'].center(13), "|", sched['FromDestination'].ljust(16), "|", sched['ToDestination'].ljust(14), "|", sched['AirplaneName'].ljust(13))

        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    def print_existing_voyages(self):
        """Prints the existing voyages"""
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

    def get_employees_not_working(self):
        boarder = Display_UI()
        boarder.print_header()
        print(f"-Employees not working-".center(140))
        print()
        day = input("Enter date &&/&&/&&&&: ")
        print(constants.DASH * 140)
        print("Name".center(30),"|", "SSN".center(15), "|", "Rank".center(25), "|", "Licence".center(35), "|", "Phone Number".center(15))
        print(constants.DASH * 140)
        employees_not_working = self.logic_wrapper.get_employees_not_working(day)
        for employee in employees_not_working:

            if employee['licence'] == " ":
                print(employee['Name'].ljust(30),"|", employee['SSN'].center(15), "|", employee['Rank'].ljust(25), "|", "N/A".ljust(35), "|", employee['PhoneNumber'].center(15))
            else:
                print(employee['Name'].ljust(30),"|", employee['SSN'].center(15), "|", employee['Rank'].ljust(25), "|", employee['licence'].ljust(35), "|", employee['PhoneNumber'].center(15))
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()

    def get_employees_working(self):
        boarder = Display_UI()
        boarder.print_header()
        print(f"-Employees not working-".center(140))
        print()
        day = input("Enter date &&/&&/&&&&: ")
        print(constants.DASH * 140)
        print("Name".center(30),"|", "SSN".center(15), "|", "Rank".center(25), "|", "Licence".center(35), "|", "Phone Number".center(15))
        print(constants.DASH * 140)
        employees_working = self.logic_wrapper.get_employees_working(day)
        for employee in employees_working:

            if employee['licence'] == " ":
                print(employee['Name'].ljust(30),"|", employee['SSN'].center(15), "|", employee['Rank'].ljust(25), "|", "N/A".ljust(35), "|", employee['PhoneNumber'].center(15))
            else:
                print(employee['Name'].ljust(30),"|", employee['SSN'].center(15), "|", employee['Rank'].ljust(25), "|", employee['licence'].ljust(35), "|", employee['PhoneNumber'].center(15))
        boarder.print_footer()
        print(constants.NAVBAR.center(140))
        boarder.print_footer()