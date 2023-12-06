#from Logic_Data_wrapper import data_layer.retrieve_schedule(ssn)

#employee = {"ssn", [name, rank, email, phone, landl(opt, will have just "" if not put in), licence, address]}

class EmployeeL():
    def __init__(self, ssn, name, rank, email, phone, landl, licence, address):
        self.ssn = ssn
        self.name = name
        self.rank = rank
        self.email = email       #.lstrip("+") removes leadin "+" if there is
        self.phone = phone
        self.landl = landl
        self.licence = licence
        self.employee = {}
        
    def create_employee(self):
        self.employee[self.ssn] = [self.name, self.rank, self.email, self.phone, self.landl, self.licence]
        
    def get_employee_info(self, ssn):
        return self.data_wrapper.get_data(ssn)
        
    
    def get_schedule(self):
        #schedule = data_layer.retrieve_schedule(ssn)
        #return schedule
        pass
    
    def get_request_time_off(self):
        pass # C level
    
    def edit_employee_info(self):
        pass
        