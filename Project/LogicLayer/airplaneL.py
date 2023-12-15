from dataLayer.logic_data_wrapper import LogicDataWrapper
#from models.airplaneM import Airplanes

class AirplaneL:
    def __init__(self):
        self.data_wrapper = LogicDataWrapper()

    def create_airplane(self, airplane):
        self.data_wrapper.create_airplane(airplane)
        
    def get_plane_info(self, airplane_name):
        return self.data_wrapper.get_airplane_info(airplane_name)

    def get_airplane_list(self):
        return self.data_wrapper.get_airplane_list()

#    def edit_airplane_info(self, airplane_name, update_info):
#        if not self.data_wrapper.get_airplane_info(airplane_name):
#            return False
#        return self.data_wrapper.edit_airplane(airplane_name, update_info)
