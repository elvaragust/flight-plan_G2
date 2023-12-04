#from data. import
#from import

class VoyageL:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def create_voyage(self, voyage):
        self.data_wrapper.create_voyage(voyage)

    def edit_voyage(self, voyage_id, updated_voyage):
        existing_voyage = self.data_wrapper.get_voyage(voyage_id)
        if not existing_voyage:
            return False
        
        return self.data_wrapper.update_voyage(voyage_id, updated_voyage)

    def get_flight_info(self, flight_number):
        return self.data_wrapper.get_flight_info(flight_number)

    def get_employee_list(self):
        return self.data_wrapper.get_employee_list()

    def get_airplane_list(self, ):
        return self.data_wrapper.get_airplane_list()

    def find_flight_by_number(self, flight_number):
        return self.data_wrapper.find_flight_by_type(flight_number)
