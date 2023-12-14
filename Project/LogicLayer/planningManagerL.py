from dataLayer.logic_data_wrapper import LogicDataWrapper

class PlanningManagerL:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def register_voyage(self, voyage_info):
        self.data_wrapper.create_voyage(voyage_info)

    def register_flight(self, flight_info):
        self.data_wrapper.create_flight(flight_info)

    def register_airplane(self, airplane_info):
        self.data_wrapper.create_airplane(airplane_info)

    def get_airplane_list(self):
        return self.data_wrapper.get_airplane_list()

    def get_voyage(self, voyage_id):
        return self.data_wrapper.get_voyage(voyage_id)

