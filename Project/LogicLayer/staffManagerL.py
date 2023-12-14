from dataLayer.logic_data_wrapper import LogicDataWrapper


class staffManagerL:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def register_employee(self, employee_info):
        self.data_wrapper.create_employee(employee_info)

    def create_schedule(self, schedule_info):
        self.data_wrapper.create_schedule(schedule_info)

    def edit_schedule(self, schedule_id, update_info):
        self.data_wrapper.update_schedule(schedule_id, update_info)

    def get_employee_list(self):
        return self.data_wrapper.get_employee_list()

    def get_schedule(self, schedule_id):
        return self.data_wrapper.get_schedule(schedule_id)

