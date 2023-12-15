
class ValidationL():
    
    def validate_employee_name(self, name):
        """ validates the name of the employee
        
        args: name of the employee
        
        returns: True if the name is valid
        
        """
        name_without_spaces = name.replace(' ', '')
        if name_without_spaces == "":
            raise ValueError("Name cannot be empty")
        
        if not name_without_spaces.isalpha():
            raise ValueError("Cannot have a number")
        
        elif len(name) > 40:
            raise ValueError("Name cannot be longer than 50 characters")
        
        else:
            return True
        
        
    def validate_employee_rank(self, rank):
        """ validates the rank of the employee
        
        args: rank of the employee
        
        returns: True if the rank is valid
        
        """
        rank_without_spaces = rank.replace(' ', '')
        
        if rank_without_spaces == "":
            raise ValueError("Rank cannot be empty")
        
        elif len(rank) > 20:
            raise ValueError("Rank cannot be more than 20 characters")
        
        else:
            return True
        
        
    def validate_email(self, email):
        """ validates the email of the employee
        
        args: email of the employee
        
        returns: True if the email is valid
        
        """
        if "@" not in email:
            raise ValueError("Email needs to have a: @")
        
        elif "." not in email:
            raise ValueError("Email needs to have a: .")
        
        elif len(email) > 40:
            raise ValueError("Email cannot be more than 40 characters")
        
        else:
            return True
        
        
    def validate_phone(self, phone):
        """ validates the phone of the employee
        
        args: phone of the employee
        
        returns: True if the phone is valid
        
        """
        if phone[0] == "+":
            raise ValueError("Phone number should not have the area code")
        
        elif len(phone) != 7:
            raise ValueError("Phone number should contain 7 numbers")
        
        elif not phone.isdigit():
            raise ValueError("Phone numbe rcan only contain digits")
        
        else:
            return True
        
    def validate_employee_landline(self, phone):
        """ validates the phone of the employee
        
        args: phone of the employee
        
        returns: True if the phone is valid
        
        """
        if phone[0] == "+":
            raise ValueError("Phone number should not have the area code")
        
        elif len(phone) != 7:
            raise ValueError("Phone number should contain 7 numbers")
        
        elif not phone.isdigit():
            raise ValueError("Phone numbe rcan only contain digits")
        
        else:
            return True
    
    
    def validate_date(self, date):
        """ validates date
        
        args: date
        
        returns: True if the date is valid
        
        """
        date_validation = [int(i) for i in date.split("/")]
        
        if not date_validation.isdigit():
            raise ValueError("Can only be numbers between the /")
        #day
        if date_validation[0] > 31:
            raise ValueError("Day does not exist, need to be (1-31)")
        #month
        elif date_validation[1] > 12:
            raise ValueError("Month does not exist, needs to be (1-12)")
        #year
        elif date_validation[2] < 23:
            raise ValueError("Year does not exist, cannot be in the past")
        
        
    def validate_time(self, time):
        """ validates the time
        
        args: time
        
        returns: True if the time is valid
        
        """
        time_validation = [int(i) for i in time.split(":")]
        
        if not time_validation.isdigit():
            raise ValueError("Can only contain numbers between the :")
        
        if time_validation[0] > 23:
            raise ValueError("Hour does not exist")
        
        if time_validation[1] > 60:
            raise ValueError("Minute does not exist")
        
        else:
            return True
        
    def validate_licence(self, pilot_license):
        """ validates the licence of the employee
        
        args: licence of the employee
        
        returns: True if the licence is valid
        
        """
        licence_without_spaces = pilot_license.replace(' ', '')
        
        if licence_without_spaces == "":
            raise ValueError("Licence cannot be empty")
        
        elif len(pilot_license) > 40:
            raise ValueError("Licence cannot be more than 40 characters")
        
        else:
            return True

#    def vaildate_gate(self, gate):
#        if not gate[1].isdigit:
#            raise ValueError("Gate number incorrect")
        
#        elif len(gate) == 3:
#            if not gate[2].isdigit:
#                raise ValueError("Gate number incorrect")
        
#        elif gate[0].isdigit:
#            raise ValueError("Gate number incorrect")
        
#        else:
#            return True
    

    #def vaildate_booked_seats(self, seats):
    #    pass
    
    #def validate_avalable_seats(self, seats):
    #    pass

    #def validate_airport(self, airport):
    #    pass
    
#    def validate_plane_status(self, airplane):
        # in flight, in repair, on ground 
#        pass       
        
    def validate_employee_address(self, address):
        """ validates the address of the employee
        
        args: address of the employee
        
        returns: True if the address is valid
        
        """
        if address == "":
            raise ValueError("Address cannot be empty")
        elif len(address) > 50:
            raise ValueError("Address cannot be longer than 50 characters")
        else:
            return True
    
    
    def validate_employee_ssn(self, ssn):
        """ validates the ssn of the employee
        
        args: ssn of the employee
        
        returns: True if the ssn is valid
        
        """
        if ssn == "":
            raise ValueError("SSN cannot be empty")
        
        elif not ssn.isdigit():
            raise ValueError("Can only be numbers")
        
        elif len(ssn) != 10:
            raise ValueError("SSN must be 10 characters long")
        
        else:
            return True

    