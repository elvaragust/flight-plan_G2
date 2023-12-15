from dataLayer.logic_data_wrapper import LogicDataWrapper
#from models.airplaneM import Airplanes

class AirplaneL:
    def __init__(self):
        self.data_wrapper = LogicDataWrapper()

    def create_airplane(self, airplane):
        """ creates an airplane and saves it to the csv file
        
        args: airplane object
        
        returns: None
        
        """
        self.data_wrapper.create_airplane(airplane)
        
    def get_plane_info(self, airplane_name):
        """ finds an airplane by name and returns it
        
        args: name of the airplane
        
        returns: airplane object
        
        """
        return self.data_wrapper.get_airplane_info(airplane_name)

    def get_airplane_list(self):
        """ returns a list of all airplanes
        
        args: None
        
        returns: list of all airplanes
        
        """
        return self.data_wrapper.get_all_airplanes()

#    def edit_airplane_info(self, airplane_name, update_info):
#        if not self.data_wrapper.get_airplane_info(airplane_name):
#            return False
#        return self.data_wrapper.edit_airplane(airplane_name, update_info)
