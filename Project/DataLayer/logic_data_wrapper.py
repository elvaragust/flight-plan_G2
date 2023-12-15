from dataLayer.employeeD import EmployeeData
from dataLayer.airplaneD import AirplaneData
from dataLayer.flightD import FlightData
from dataLayer.voyageD import VoyageData

class LogicDataWrapper:
    def __init__(self):
        self.employee_data = EmployeeData()
        self.airplane_data = AirplaneData()
        self.flight_data = FlightData()
        self.voyage_data = VoyageData()
    
    
    
    def create_airplane(self, airplane_info):
        self.airplane_data.create_employee(airplane_info)
    
    def get_airplane_info(self, airplane_name):
        return self.airplane_data.get_employee_by_name(airplane_name)
    
    def get_all_airplanes(self):
        return self.airplane_data.get_all_airplanes()





    def create_employee(self, employee_info):
        self.employee_data.create_employee(employee_info)

    def get_employee_info(self, ssn):
        return self.employee_data.get_employee_by_id(ssn)

    def get_schedule_info(self, ssn):
        return self.employee_data.get_schedule_by_ssn(ssn)
    
    def get_all_employees(self):
        return self.employee_data.get_all_employees()




    def create_flight(self, flight_info):
        self.flight_data.create_flight(flight_info)

    def assign_staff(self, flight_id, ssn):
        self.flight_data.assign_staff_to_flight(flight_id, ssn)

    def get_flight_info(self, flight_id):
        return self.flight_data.get_flight_by_id(flight_id)

    def get_all_flights(self):
        return self.flight_data.get_all_flights()




    def create_voyage(self, voyage_info):
        self.voyage_data.create_voyage(voyage_info)
    
    def get_voyage_by_id(self, voyage_id):
        return self.voyage_data.get_voyage_by_id(voyage_id)

    def get_all_voyages(self):
        return self.voyage_data.get_all_voyages()
    
    
    
    
    
    def create_schedule(self, schedule_info):
        self.employee_data.create_schedule(schedule_info)

    def update_schedule(self, schedule_id, update_info):
        self.employee_data.update_schedule(schedule_id, update_info)

    def get_employee_list(self):
        return self.employee_data.get_all_employees()
    
    def get_schedule(self, schedule_id):
        return self.employee_data.get_schedule(schedule_id)


