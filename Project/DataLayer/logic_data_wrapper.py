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
        """ creates an airplane and saves it to the csv file
        
        args: airplane object
        
        returns: None
        
        """
        self.airplane_data.create_employee(airplane_info)
    
    def get_airplane_info(self, airplane_name):
        """ finds an airplane by name and returns it
        
        args: name of the airplane
        
        returns: airplane object
        
        """
        return self.airplane_data.get_employee_by_name(airplane_name)
    
    def get_all_airplanes(self):
        """ returns a list of al airplanes
        
        args: None
        
        returns: list of all airplanes
        
        """
        return self.airplane_data.get_all_airplanes()





    def create_employee(self, employee_info):
        """ creates an employee and saves it to the csv file
        
        args: employee object
        
        returns: None
        
        """
        self.employee_data.create_employee(employee_info)

    def get_employee_info(self, ssn):
        """ finds an employee by id and returns it
        
        args: id of the employee
        
        returns: employee object
        
        """
        return self.employee_data.get_employee_by_id(ssn)

    def get_schedule_info(self, ssn):
        """ finds an employee by id and returns it
        
        args: id of the employee
        
        returns: employee object
        
        """
        return self.employee_data.get_schedule_by_ssn(ssn)
    
    def edit_employee(self, ssn, new_employee):
        """ finds an employee by id and returns it
        
        args: id of the employee
        
        returns: mployee object
        
        """
        return self.employee_data.edit_employee_by_id(ssn, new_employee)
    
    def get_all_employees(self):
        """ returns a list of all mployees
        
        args: None
        
        returns: list of all employees
        
        """
        return self.employee_data.get_all_employees()
    




    def create_flight(self, flight_info):
        """ creates an flight and saves it to the csv file
        
        args: flight object
        
        returns: None
        
        """
        self.flight_data.create_flight(flight_info)

    def assign_staff(self, flight_id, ssn):
        """ assigns staff to a flight
        
        args: flight id and ssn of employee
        
        returns: None
        
        """
        self.flight_data.assign_staff_to_flight(flight_id, ssn)

    def get_flight_info(self, flight_id):
        """ finds an flight by id and returns it
        
        args: id of the flight
        
        returns: flight object
        
        """
        
        return self.flight_data.get_flight_by_id(flight_id)

    def get_all_flights(self):
        """ returns a list of all flights
        
        args: None
        
        returns: list of all flights
        
        """
        return self.flight_data.get_all_flights()




    def create_voyage(self, voyage_info):
        """ creates a voyage and saves it to the csv file
        
        args: voyage object
        
        returns: None
        
        """
        self.voyage_data.create_voyage(voyage_info)
    
    def get_voyage_by_id(self, voyage_id):
        """ finds a voyage by id and returns it
        
        args: id of the voyage
        
        returns: voyage object
        
        """
        return self.voyage_data.get_voyage_by_id(voyage_id)

    def get_all_voyages(self):
        """ returns a list of all voyages
        
        args: None
        
        returns: list of all voyages
        
        """
        return self.voyage_data.get_all_voyages()
    
    
    
    
    
    def create_schedule(self, schedule_info):
        """ creates a schedule and saves it to the csv file
        
        args: shcedule object
        
        returns: None
        
        """
        self.employee_data.create_schedule(schedule_info)

    def update_schedule(self, schedule_id, update_info):
        """ updates a schedule and saves it to the csv file
        
        args: shcedule id and update info
        
        returns: None
        
        """
        self.employee_data.update_schedule(schedule_id, update_info)

    def get_employee_list(self):
        """ returns a list of all employees
        
        args: None
        
        returns: list of all employeees
        
        """
        return self.employee_data.get_all_employees()
    
    def get_schedule(self, schedule_id):
        """ finds a schedule by id and returns it
        
        args: id of the schedule
        
        returns: schedule object
        
        """
        return self.employee_data.get_schedule(schedule_id)


