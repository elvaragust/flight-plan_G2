from dataLayer.logic_data_wrapper import LogicDataWrapper

class PlanningManagerL:
    def __init__(self, data_wrapper):
        self.data_wrapper = LogicDataWrapper()

    def register_voyage(self, voyage_info):
        """ creates a voyage and saves it to the cds file
        
        args: voyage object
        
        returns: None
        
        """
        self.data_wrapper.create_voyage(voyage_info)

    def register_flight(self, flight_info):
        """ creates a flight and saves it to the cvs file
        
        args: flight object
        
        returns: None
        
        """
        self.data_wrapper.create_flight(flight_info)

    def register_airplane(self, airplane_info):
        """ creates an airplane and saves it to the csv file
        
        args: airplane object
        
        returns: None
        
        """
        self.data_wrapper.create_airplane(airplane_info)

    def get_airplane_list(self):
        """ returns a list of all airplanes
        
        args: None
        
        returns: list of all airplanes
        
        """
        return self.data_wrapper.get_airplane_list()

    def get_voyage(self, voyage_id):
        """ finds a voyage by id and returns it
        
        args: id of the voyage
        
        returns: voyage object
        
        """
        return self.data_wrapper.get_voyage(voyage_id)

