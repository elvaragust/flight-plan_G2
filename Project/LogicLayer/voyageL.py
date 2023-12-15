from dataLayer.logic_data_wrapper import LogicDataWrapper


class VoyageL:
    def __init__(self, data_wrapper): #: DataWrapper
        self.data_wrapper = data_wrapper

    def create_voyage(self, voyage):
        """ creates a voyage and saves it to the csv file
        
        args: voyage object
        
        returns: None
        
        """
        self.data_wrapper.create_voyage(voyage)

    def edit_voyage(self, voyage_id, update_info):
        """ edits a voyage and saves it to the csv file
        
        args: voyage id and update info
        
        returns: None
        
        """
        existing_voyage = self.data_wrapper.get_voyage_info(voyage_id)
        if not existing_voyage:
            return False
        
        return self.data_wrapper.update_voyage(voyage_id, update_info)

    def get_flight_info(self, flight_number):
        """ finds an flight by flight_number and returns it
        
        args: flight_number of the flight
        
        returns: flight object
        
        """
        return self.data_wrapper.get_flight_info(flight_number)

    def get_employee_list(self):
        """ returns a list of all employees
        
        args: None
        
        returns: list of all employees
        
        """
        return self.data_wrapper.get_employee_list()

    def get_airplane_list(self):
        """ returns a list of all airplanes
        
        args: None
        
        returns: list of all airplanes
        
        """
        return self.data_wrapper.get_airplane_list()

    def find_flight_by_number(self, flight_number):
        """ returns a list of all airplanes
        
        args: None
        
        returns: list of all airplanes
        
        """
        return self.data_wrapper.find_flight_by_number(flight_number)
