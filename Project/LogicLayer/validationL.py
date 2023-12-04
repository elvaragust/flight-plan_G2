#This 

class ValidationL():
    
    def validate_employee_name(self, name):
        if name == "":
            raise ValueError("Name cannot be empty")
        elif len(name) > 50:
            raise ValueError("Name cannot be longer than 50 characters")
        else:
            return True
        
    def validate_employee_rank(self, rank):
        pass

    def validate_email(self, email):
        pass
    
    def validate_phone(self, phone):
        pass
    
    def validate_date(self, date):
        pass
    
    def validate_time(self, time):
        pass
    
    def vaildate_gate(self, gate):
        pass
    
    def validate_seats(self, seats):
        pass
    
    def vaildate_booked_seats(self, seats):
        pass
    
    def validate_avalable_seats(self, seats):
        pass

    def validate_airport(self, airport):
        pass
    
    def validate_plane_status(self, airplane):
        pass       
        
    def validate_employee_address(self, address):
        if address == "":
            raise ValueError("Address cannot be empty")
        elif len(address) > 50:
            raise ValueError("Address cannot be longer than 50 characters")
        else:
            return True
    
    
    def validate_employee_ssn(self, ssn):
        if ssn == "":
            raise ValueError("SSN cannot be empty")
        elif len(ssn) != 10:
            raise ValueError("SSN must be 10 characters long")
        else:
            return True

    