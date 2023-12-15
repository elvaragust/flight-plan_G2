from dataLayer.logic_data_wrapper import LogicDataWrapper

class EmployeeL():
    def __init__(self):
        self.data_wrapper = LogicDataWrapper()

    def create_employees(self, employee):
        """ creates an employee and saves it to the csv file
        
        args: employee object
        
        returns: None
        
        """
        self.data_wrapper.create_employee(employee)
        
    def get_employee_info(self, ssn):
        """ finds an employee by ssn and returns it
        
        args: ssn of the employee
        
        returns: employee object
        
        """
        return self.data_wrapper.get_employee_info(ssn)
        
    def get_schedule(self, ssn):
        """ finds an employee by ssn and returns it
        
        args: ssn of the employee
        
        returns: employee object
        
        """
        return self.data_wrapper.get_schedule_info(ssn)
    
    def get_request_time_off(self, ssn):
        """ finds an employee by ssn and returns it
        
        args: ssn of the employee
        
        returns: employee object
        #UNFINISHED
        
        """
        pass # C level
    
    def edit_employee_info(self, ssn, new_employee):
        """ edits an employee and saves it to the csv file
        
        args: employee object
        
        returns: None
        
        """
        existing_employee = self.data_wrapper.get_employee_info(ssn)
        if not existing_employee:
            return False
        return self.data_wrapper.edit_employee_by_id(ssn, new_employee)
    
    def list_all_employees(self):
        """ returns a list of all employees
        
        args: None
        
        """
        return self.data_wrapper.get_all_employees()
    
    def see_schedule_specific(self, ssn):
        """ returns a list of all employees
        
        args: None
        
        returns: list of all employees
        
        
        """
        append_schedule = []
        schedule = self.data_wrapper.get_all_flights()
        for row in schedule:
            if row['CaptainSSN'] == ssn or row['PilotSSN'] == ssn or row['Flight_service_managerSSN'] == ssn or row['Flight_AttendantSSN'] == ssn:
                append_schedule.append(row)
        return append_schedule
