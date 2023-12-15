from employeeD import EmployeeData
from airplaneD import AirplaneData
from flightD import FlightData
from voyageD import VoyageData

class LogicDataWrapper:
    def __init__(self):
        self.employee_data = EmployeeData()
        self.airplane_data = AirplaneData()
        self.flight_data = FlightData()
        self.voyage_data = VoyageData()
    
    # airplaneL ------------------------------------------------------------
    def create_airplane(self, airplane_info):
        self.airplane_data.create_airplane(airplane_info)
    
    def get_airplane_info(self, airplane_name):
        return self.airplane_data.get_airplane_by_name(airplane_name)

#    def edit_airplane(self, airplane_name, update_info):
#        self.airplane_data.edit_airplane(airplane_name, update_info)

    # employeeL ------------------------------------------------------------
    def create_employee(self, employee_info):
        self.employee_data.create_employee(employee_info)

    def get_employee_info(self, ssn):
        return self.employee_data.get_employee_by_id(ssn)

    def get_schedule_info(self, ssn):
        return self.employee_data.get_schedule_info(ssn)

    # flightL --------------------------------------------------------------
    def create_flight(self, flight_info):
        self.flight_data.create_flight(flight_info)

    def update_flight(self, flight_number, update_info):
        self.flight_data.update_flight(flight_number, update_info)

    def assign_staff_to_flight(self, flight_number, ssn):
        self.flight_data.assign_staff_to_flight(flight_number, ssn)

    def get_flight_info(self, flight_number):
        return self.flight_data.get_flight_by_number(flight_number)

    # planningManagerL -----------------------------------------------------
    def get_airplane_list(self):
        return self.airplane_data.get_all_airplanes()

    def get_voyage_list(self):
        return self.voyage_data.get_all_voyages()
    
    # staffManagerL --------------------------------------------------------
    def create_schedule(self, schedule_info):
        self.employee_data.create_schedule(schedule_info)

    def update_schedule(self, schedule_id, update_info):
        self.employee_data.update_schedule(schedule_id, update_info)

    def get_employee_list(self):
        return self.employee_data.get_all_employees()
    
    def get_schedule(self, schedule_id):
        return self.employee_data.get_schedule(schedule_id)

    # voyageL --------------------------------------------------------------
    def create_voyage(self, voyage_info):
        self.voyage_data.create_voyage(voyage_info)

    def get_voyage_info(self, voyage_id):
        return self.voyage_data.get_voyage_by_id(voyage_id)
    
    def update_voyage(self, voyage_id, update_info):
        self.voyage_data.update_voyage(voyage_id, update_info)
    
    def find_flight_by_number(self, flight_number):
        return self.flight_data.get_flight_by_number(flight_number)