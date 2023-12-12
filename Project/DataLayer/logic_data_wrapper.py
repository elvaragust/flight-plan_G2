from DataLayerAPI import DataLayer

class LogicDataWrapper:
    def __init__(self, data_layer):
        self.data_layer = data_layer
        
    def create_employee(self, employee_info):
        self.data_layer.create_employee(employee_info)

    def get_employee_info(self, ssn):
        return self.data_layer.get_employee_by_id(ssn)

    def create_airplane(self, airplane_info):
        self.data_layer.create_airplane(airplane_info)

    def get_airplane_info(self, airplane_name):
        return self.data_layer.get_airplane_by_name(airplane_name)

    def create_voyage(self, voyage_info):
        self.data_layer.create_voyage(voyage_info)

    def get_voyage_info(self, flight_number):
        return self.data_layer.get_voyage_by_flight_number(flight_number)

    def get_employee_list(self):
        return self.data_layer.get_employee_list()

    def get_airplane_list(self):
        return self.data_layer.get_airplane_list()

    def get_voyage_list(self):
        return self.data_layer.get_voyage_list()