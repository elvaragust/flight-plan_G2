from dataLayer.logic_data_wrapper import LogicDataWrapper


class staffManagerL:
    def __init__(self, data_wrapper):
        self.data_wrapper = LogicDataWrapper()

    def register_employee(self, employee_info):
        """ creates an employee and saves it to the csv file
        
        args: employee object
        
        returns: None
        
        """
        self.data_wrapper.create_employee(employee_info)

    def create_schedule(self, schedule_info):
        """ creates a schedule and saves it to the csv file
        
        args: schedule object
        
        returns: None
        
        """
        self.data_wrapper.create_schedule(schedule_info)

    def edit_schedule(self, schedule_id, update_info):
        """ edits a schedule and saves it to the csv file
        
        args: schedule id and update info
        
        returns: None
        
        
        """
        self.data_wrapper.update_schedule(schedule_id, update_info)

    def get_employee_list(self):
        """ returns a list of all employees
        
        args: None
        
        returns: list of all employees
        
        """
        return self.data_wrapper.get_employee_list()

    def get_schedule(self, schedule_id):
        """ finds a schedule by id and returns it
        
        args: id of the schedule
        
        returns: schedule object
        
        """
        return self.data_wrapper.get_schedule(schedule_id)

