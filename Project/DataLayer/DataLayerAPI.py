import csv

from dataclasses import dataclass
from enum import Enum
from typing import Union

class Rank(Enum):
    PILOT = "pilot"
    ASSISTANT_PILOT = "assistant_pilot"
    HEAD_FLIGHT_ATTENDANT = "head_flight_attendant"
    FLIGHT_ATTENDANT = "flight_attendant"

@dataclass
class Employee:
    social_security: str
    name: str
    rank: Rank
    email: str
    phone: str
    landline: str
    license: str
    address: str

    def serialize(self) -> list[Union[str, str]]:
        return [
            self.social_security,
            self.name,
            self.rank.value,
            self.email,
            self.phone,
            self.landline,
            self.license,
            self.address
        ]
    
    @classmethod
    def from_row(cls, ssn: str, row_data: list) -> "Employee":
        return Employee(
            social_security=ssn,
            name=row_data[0],
            rank=Rank(row_data[1]),
            email=row_data[2],
            phone=int(row_data[3]),
            landline=int(row_data[4]),
            license=row_data[5],
            address=row_data[6],
        )


@dataclass
class Airplane:
    name: str
    model: str
    manufacturer: str
    seats: int

    def serialize(self) -> list[Union[str, int]]:
        return [
            self.name,
            self.model,
            self.manufacturer,
            self.total_seats
        ]

@dataclass
class Flight:
    flight_id: int
    voyage_id: int
    flight_number: str
    departure_date: str
    departure_time: int
    arriving_date: str
    arriving_time: int
    from_destination: str
    to_destination: str
    airplane_name: Airplane
    captain_ssn: int
    pilot_ssn: int
    flight_service_manager_ssn: int
    flight_attendant_ssn: int
    

    def serialize(self) -> list[Union[str, int]]:
        return [
            self.flight_id,
            self.voyage_id,
            self.flight_number,
            self.departure_date,
            self.departure_time,
            self.arriving_date,
            self.arriving_time,
            self.from_destination,
            self.to_destination,
            self.airplane_name.name,
            self.captain_ssn,
            self.pilot_ssn,
            self.flight_service_manager_ssn,
            self.flight_attendant_ssn
            
        ]
@dataclass
class Voyage:
    voyage_id: int
    destination: str
    first_flight_date: str
    last_flight_date: str

    def serialize(self) -> list[Union[str, int]]:
        return [
            self.voyage_id,
            self.destination,
            self.first_flight_date,
            self.last_flight_date
        ]


class DataLayer:
    employees = {}
    airplanes = {}
    voyages = {}

    def create_employee(self, employee):
        self.employees[employee.social_security] = employee.serialize()

    def get_employee_by_id(self, social_security):
        return self.employees.get(social_security, None)

    def create_airplane(self, airplane):
        self.airplanes[airplane.name] = airplane.serialize()

    def get_airplane_by_name(self, airplane_name):
        return self.airplanes.get(airplane_name, None)

    def create_voyage(self, voyage):
        self.voyages[voyage.flight_number] = voyage.serialize()

#    def get_voyage_by_flight_number(self, flight_number):
#        for voyage in self.voyages:
#            if voyage.flight_number == flight_number:
#                return voyage
#        return None
    
    def get_employee_list(self):
        return self.employees

    def get_airplane_list(self):
        return self.airplanes

    def get_voyage_list(self):
        return self.voyages

def read_csv_to_dict(file_name):
    data_dict = {}
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # thsi skips the header row
        for row in reader:
            key = row[0]
            value = row[1:]
            data_dict[key] = value
    return data_dict

def main():
    
    EMPLOYEE_FILE_NAME = "employee.csv"
    employees = read_csv_to_dict(EMPLOYEE_FILE_NAME)
    
    AIRPLANE_FILE_NAME = "airplanes.csv"
    airplanes = read_csv_to_dict(AIRPLANE_FILE_NAME)
    
    FLIGHT_FILE_NAME = "flight.csv"
    flights = read_csv_to_dict(FLIGHT_FILE_NAME)
    
    VOYAGE_FILE_NAME = "voyages.csv"
    voyages = read_csv_to_dict(VOYAGE_FILE_NAME)
    
    
    with open(EMPLOYEE_FILE_NAME, 'w', newline='') as csvfile:
        employee_write = csv.writer(csvfile)
        for key, value in employees.items():
            employee_write.writerow([key] + value)
    
    with open(AIRPLANE_FILE_NAME, 'w', newline='') as csvfile:
        airplane_write = csv.writer(csvfile)
        for key, value in airplanes.items():
            airplane_write.writerow([key] + value)

    with open(FLIGHT_FILE_NAME, "w", newline="") as csvfile:
        flight_write = csv.writer(csvfile)
        for key, value in flights.items():
            flight_write.writerow([key] + value)

    with open(VOYAGE_FILE_NAME, newline='') as csvfile:
        voyage_write = csv.writer(csvfile)
        for key, value in voyages.items():
            voyage_write.writerow([key] + value)

    print(f"Data prepared for {EMPLOYEE_FILE_NAME}")
    print(f"Data prepared for {AIRPLANE_FILE_NAME}")
    print(f"Data prepared for {VOYAGE_FILE_NAME}")
    print(f"Data prepared for {EMPLOYEE_FILE_NAME}")

if __name__ == "__main__":
    main()