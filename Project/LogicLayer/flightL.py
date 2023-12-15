from dataLayer.logic_data_wrapper import LogicDataWrapper


class FlightL():
    def __init__(self, data_wrapper):
        self.data_wrapper = LogicDataWrapper()
        
    def create_flight(self, flight):
        self.data_wrapper.create_flight(flight)
    
    def edit_flight(self, flight_number, update_info):
        #flight = data_layer.retrieve_schedule(ssn)
        #return flight
        existing_flight = self.data_wrapper.get_voyage_info(flight_number)
        if not existing_flight:
            return False
        
        return self.data_wrapper.update_flight(flight_number, update_info)
    
    def assign_staff(self):
        pass
    
    def get_flight_info(self, flight_number):
        return self.data_wrapper.get_flight_info(flight_number)
    