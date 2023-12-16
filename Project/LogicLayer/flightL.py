from dataLayer.logic_data_wrapper import LogicDataWrapper
from datetime import datetime

class FlightL():
    def __init__(self, data_wrapper=None):
        if data_wrapper is None:
            self.data_wrapper = LogicDataWrapper()
        else:
            self.data_wrapper = data_wrapper
        
    def create_flight(self, flight):
        """ creates an flight and saves it to the csv file
        
        args: flight object
        
        returns: None
        
        """
        self.data_wrapper.create_flight(flight)
    
    def edit_flight(self, flight_number, update_info):
        """ edits an flight and saves it to the csv file
        
        args: flight object
        
        returns: None
        
        """
        #flight = data_layer.retrieve_schedule(ssn)
        #return flight
        existing_flight = self.data_wrapper.get_voyage_info(flight_number)
        if not existing_flight:
            return False
        
        return self.data_wrapper.update_flight(flight_number, update_info)
    
    def assign_staff(self):
        """ assigns staff to a flight
        
        args: flight object
        
        returns: None
        #UNIFINISHED
        
        """
        pass
    
    def get_flight_info(self, flight_number):
        """ finds an flight by flight_number and returns it
        
        args: flight_number of the flight
        
        returns: flight object
        
        """
        return self.data_wrapper.get_flight_info(flight_number)
        
    def get_employees_not_working(self, day):
        """ finds an employee by ssn and returns it
        
        args: ssn of the employee
        
        returns: employee object
        
        """
        day = datetime.strptime(day, '%d/%m/%Y')
        flights = self.data_wrapper.get_all_flights()
        employees = self.data_wrapper.get_all_employees()

        working_employees = set()
        for flight in flights:
            if 'DepartureDate' in flight:
                flight_day = datetime.strptime(flight['DepartureDate'], '%d/%m/%Y')
                if flight_day.date() == day.date():
                    working_employees.add(flight['CaptainSSN'])
                    working_employees.add(flight['PilotSSN'])
                    working_employees.add(flight['Flight_service_managerSSN'])
                    working_employees.add(flight['Flight_AttendantSSN'])

        employees_not_working = [employee for employee in employees if employee['SSN'] not in working_employees]
        return employees_not_working
    
    def get_employees_working(self, day):
        """ finds an employee by ssn and returns it
        
        args: ssn of the employee
        
        returns: employee object
        
        """
        day = datetime.strptime(day, '%d/%m/%Y')
        flights = self.data_wrapper.get_all_flights()
        employees = self.data_wrapper.get_all_employees()

        working_employees = set()
        for flight in flights:
            if 'DepartureDate' in flight:
                flight_day = datetime.strptime(flight['DepartureDate'], '%d/%m/%Y')
                if flight_day.date() == day.date():
                    working_employees.add(flight['CaptainSSN'])
                    working_employees.add(flight['PilotSSN'])
                    working_employees.add(flight['Flight_service_managerSSN'])
                    working_employees.add(flight['Flight_AttendantSSN'])

        employees_not_working = [employee for employee in employees if employee['SSN'] in working_employees]
        return employees_not_working