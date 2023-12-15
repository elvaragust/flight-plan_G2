
from logicLayer.employeeL import EmployeeL

class Logic_Wrapper:
    def __init__(self) -> None:
        self.employee_logic = EmployeeL()


    def create_employee(self, employee):
        """ takes in employee object and forwarsd it to the data Layer
        
        args: employee object
        
        returns: None
        
        """
        return self.employee_logic.create_employees(employee)

    def list_all_employees(self):
        """ gets all employees
        
        args: None
        
        returns: list of all employees
        
        """
        return self.employee_logic.list_all_employees()

    def edit_employee(self, employee):
        """ takes in employee object and forwarsd it to the data Layer to edit
        
        args: employee object
        
        returns: None
        
        """
        self.employee_logic.edit_employee(employee)

    
    def get_employee_info(self, ssn):
        """ finds an employee by id and returns it
        
        args: id of the employee
        
        returns: employee object
        
        """
        return self.employee_logic.get_employee_info(ssn)
    
    def see_schedule_specific(self, ssn):
        """ finds an employee by id and returns their schedule
        
        args: id of the employee
        
        returns: schedule of the employee
        
        """
        return self.employee_logic.see_schedule_specific(ssn)


    #Airplane
    def create_airplane(self, airplane):
        """ takes in airplane object and forwards it to the data Layer
        
        args: airplane object
        
        returns: None
        
        """
        return self.airplane_logic.create_airplane(airplane)

    def get_all_airplanes(self):
        """ gets all airplanes
        
        args: None
        
        returns: list of all airplanes
        
        """
        return self.airplane_logic.get_all_airplanes()

    #Destinations

    def create_destination(self, destination):
        """ takes in destination object and forwards it to the data Layer
        
        args: destination object
        
        returns: None
        
        #UNFINISHED
        
        """
 
        self.destination_logic.create_destination(destination)

    def get_all_destinations(self):
        """ gets all destinations
        
        args: None
        
        returns: list of all destinations
        
        """
        return self.destination_logic.get_all_destinations()

        
    #Voyage
    def get_all_voyages(self):
        """ gets all voyages
        
        args: None
        
        returns: list of all voyages
        
        """
        return self.voyage.get_all_voyages()


    def create_voyage(self, voyage):
        """ creates a voyage and saves it to the csv file
        
        args: voyage object
        
        returns: None
        
        """
        
        return self.voyage.create_voyage(voyage)

