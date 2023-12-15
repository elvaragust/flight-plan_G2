import csv
from models.employeeM import Employees

class EmployeeData:
    employees = {}
    FILE_NAME = "dataLayer\\employee.csv"

    def __init__(self):
        self.load_data_from_file()
        
    def load_data_from_file(self):
        with open(self.FILE_NAME, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skips the header row
            for row in reader:
                social_security, *employee_info = row
                employee = Employees(social_security, *employee_info)
                self.employees[social_security] = employee

    def get_all_employees(self):
        employees = []
        with open(self.FILE_NAME, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employees.append(row)  # append the row directly
        return employees
            
    def save_data_to_file(self):
        with open(self.FILE_NAME, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for employee in self.employees.values():
                writer.writerow(employee.serialize())

    def create_employee(self, employee: Employees):
        self.employees[employee.social_security] = employee
        self.save_data_to_file()

    def get_employee_by_id(self, social_security):
        return self.employees.get(social_security, None)

    def get_employee_list(self):
        return list(self.employees.values())
    
    def see_schedule_specific(self, ssn):
        pass       
