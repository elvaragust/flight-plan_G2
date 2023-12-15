from dataLayer.logic_data_wrapper import LogicDataWrapper

class EmployeeL():
    def __init__(self, data_wrapper):
        self.data_wrapper = LogicDataWrapper()

    def create_employees(self, employee):
        self.data_wrapper.create_employee(employee)
        
    def get_employee_info(self, ssn):
        return self.data_wrapper.get_employee_info(ssn)
        
    def get_schedule(self, ssn):
        #schedule = data_layer.retrieve_schedule(ssn)
        #return schedule
        return self.data_wrapper.get_schedule_info(ssn)
    
    def get_request_time_off(self):
        pass # C level
    
#    def edit_employee_info(self, ssn, update_info):
#        existing_employee = self.data_wrapper.get_employee_info(ssn)
#        if not existing_employee:
#            return False
#        return self.data_wrapper.update_employee(update_info)
        