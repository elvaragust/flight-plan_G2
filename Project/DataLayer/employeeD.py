import csv
from models.employeeM import Employees

class EmployeeData:
    employees = {}
    FILE_NAME = "dataLayer\\employee.csv"

    def __init__(self):
        pass
        
#    def load_data_from_file(self):
#        with open(self.FILE_NAME, newline='') as csvfile:
#            reader = csv.reader(csvfile)
#            next(reader)  # Skips the header row
#            for row in reader:
#                social_security, *employee_info = row
#                employee = Employees(social_security, *employee_info)
#                self.employees[social_security] = employee

    def get_all_employees(self):
        """ returns a list of all mployees
        
        args: None
        
        returns: list of all employees
        
        """
        employee_list = []
        with open(self.FILE_NAME, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employee_list.append(row)
        return employee_list
            
    def save_data_to_file(self):
        """ saves the employee list to the csv file
        
        args: None
        
        returns: None
        
        """
        
        with open(self.FILE_NAME, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for employee in self.employees.values():
                writer.writerow(employee.serialize())

    def create_employee(self, employee: Employees):
        """ creates an employee and saves it to the csv file
        
        args: employee object
        
        returns: None
        
        """
        self.employees[employee.social_security] = employee
        self.save_data_to_file()

    def get_employee_by_id(self, ssn):
        """ finds an employee by id and returns it
        
        args: id of the employee
        
        returns: employee object
        
        """
        with open(self.FILE_NAME, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['SSN'] == ssn:
                    return row
        return None
    
    def edit_employee_by_id(self, ssn, new_employee):
        """ finds an employee by id and replaces it with the new employee
        
        args: ssn of the employee and new_employee which is a dictionary
        
        returns: new employee
        
        """
        employee_list = []
        with open(self.FILE_NAME, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['SSN'] != ssn:
                    employee_list.append(row)
                else:
                    employee_list.append(new_employee)
        with open(self.FILE_NAME, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['SSN', 'Name', 'Role', 'Rank', 'License', 'Address', 'Phone', 'Email']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(employee_list)
        return new_employee

    def get_employee_list(self):
        """ returns a list of all employees
        
        args: None
        
        returns: list of all employees
        
        """
        return list(self.employees.values())
