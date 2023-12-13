from DataLayerAPI import DataLayer

class LogicDataWrapper:
    def __init__(self, data_layer):
        self.data_layer = data_layer
    
    # airplaneL ------------------------------------------------------------
    def create_airplane(self, airplane_info):
        self.data_layer.create_airplane(airplane_info)
    
    def get_airplane_info(self, airplane_name):
        return self.data_layer.get_airplane_by_name(airplane_name)

    def edit_airplane(self, airplane_name, update_info):
        pass

    # employeeL ------------------------------------------------------------
    def create_employee(self, employee_info):
        self.data_layer.create_employee(employee_info)

    def get_employee_info(self, ssn):
        return self.data_layer.get_employee_by_id(ssn)

    def get_schedule_info(ssn):
        pass

    # flightL --------------------------------------------------------------
    def create_flight(self, flight):
        pass

    def update_flight(self, flight_number, update_info):
        pass

    def assign_staff_to_flight(self, flight_number, ssn):
        pass

    def get_flight_info(self, flight_number):
        pass

    # planningManagerL -----------------------------------------------------
    def get_airplane_list(self):
        return self.data_layer.get_airplane_list()

    def get_voyage_list(self):
        return self.data_layer.get_voyage_list()
    
    # staffManagerL --------------------------------------------------------
    def create_schedule(self, schedule_info):
        pass

    def update_schedule(self, schedule_id, update_info):
        pass

    def get_employee_list(self):
        return self.data_layer.get_employee_list()
    
    def get_schedule(self, schedule_id):
        pass

    # voyageL --------------------------------------------------------------
    def create_voyage(self, voyage_info):
        self.data_layer.create_voyage(voyage_info)

    def get_voyage_info(self, flight_number):
        return self.data_layer.get_voyage_by_flight_number(flight_number)
    
    def update_voyage(voyage_id, update_info):
        pass
    
    def find_flight_by_number(self, flight_number):
        pass