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
    name: str
    rank: Rank
    email: str
    social_security: int
    phone: int
    license: str
    home_address: str

    def serialize(self) -> list[Union[str, int]]:
        return [
            self.name,
            self.rank.value,
            self.email,
            self.social_security,
            self.phone,
            self.license,
            self.home_address
        ]
    
    @classmethod
    def from_row(cls, row_data: list[str]) -> "Employee":
        return Employee(
            name=row_data[1],
            rank=Rank(row_data[2]),
            email=row_data[3],
            social_security=int(row_data[4]),
            phone=int(row_data[5]),
            license=row_data[6],
            home_address=row_data[7],
        )


@dataclass
class Airplane:
    name: str
    total_seats: int
    booked_seats: int
    available_seats: int

    def serialize(self) -> list[Union[str, int]]:
        return [
            self.name,
            self.total_seats,
            self.booked_seats,
            self.available_seats
        ]

@dataclass
class Voyage:
    flight_number: str
    departure_date: str
    departure_time: int
    arriving_date: str
    arriving_time: int
    destination: str
    gate: str
    airplane: Airplane
    employees: list[Employee]

    def serialize(self) -> list[Union[str, int]]:
        return [
            self.flight_number,
            self.departure_date,
            self.departure_time,
            self.arriving_date,
            self.arriving_time,
            self.destination,
            self.gate,
            self.airplane.name,  
            [employee.social_security for employee in self.employees]  
        ]


class DataLayer:
    employees = []
    airplanes = []
    voyages = []

    def create_employee(self, employee):
        self.employees.append(employee)

    def get_employee_by_id(self, social_security):
        for employee in self.employees:
            if employee.social_security == social_security:
                return employee
        return None

    def create_airplane(self, airplane):
        self.airplanes.append(airplane)

    def get_airplane_by_name(self, airplane_name):
        for airplane in self.airplanes:
            if airplane.name == airplane_name:
                return airplane
        return None

    def create_voyage(self, voyage):
        self.voyages.append(voyage)

    def get_voyage_by_flight_number(self, flight_number):
        for voyage in self.voyages:
            if voyage.flight_number == flight_number:
                return voyage
        return None
    
    def get_employee_list(self):
        return self.employees

    def get_airplane_list(self):
        return self.airplanes

    def get_voyage_list(self):
        return self.voyages

def main():
    EMPLOYEE_FILE_NAME = "employees.csv"
    employees: list[Employee] = []
    with open(EMPLOYEE_FILE_NAME, newline='') as csvfile:
        employee_reader = csv.reader(csvfile, )
        for row in employee_reader:
            employees.append(Employee.from_row(row))

    print(f"{len(employees)} number of employees from {EMPLOYEE_FILE_NAME}")

    new_employee = Employee(
        "1", "Jón", Rank.PILOT, "Jón@nanair.is", "0101902009", "5812345", "Boeing Max8", "Dufnaholar 10"
    )

    employees.append(new_employee)

    with open(EMPLOYEE_FILE_NAME, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for employee in employees:
            csv_writer.writerow(employee.serialize())

    AIRPLANE_FILE_NAME = "airplanes.csv"
    airplanes: list[Airplane] = []
    with open(AIRPLANE_FILE_NAME, newline='') as csvfile:
        airplane_reader = csv.reader(csvfile)
        for row in airplane_reader:
            airplanes.append(Airplane(*row))

    VOYAGE_FILE_NAME = "voyages.csv"
    voyages: list[Voyage] = []
    with open(VOYAGE_FILE_NAME, newline='') as csvfile:
        voyage_reader = csv.reader(csvfile)
        for row in voyage_reader:
            airplane_name = row[7]  
            airplane = DataLayer.get_airplane_by_name(airplane_name)
            employee_ids = row[8]  
            employees = [DataLayer().get_employee_by_social_security(int(ssn)) for ssn in employee_ids]
            voyages.append(Voyage(*row[:7], airplane, employees))


    print(f"Wrote to {EMPLOYEE_FILE_NAME}")
    print(f"Wrote to{AIRPLANE_FILE_NAME}")
    print(f"Wrote to{VOYAGE_FILE_NAME}")
    print(f"Wrote to {EMPLOYEE_FILE_NAME}")


if __name__ == "__main__":
    main()