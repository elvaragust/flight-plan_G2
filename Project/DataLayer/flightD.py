import csv
from datetime import datetime
from Models.flightM import Flight

class FlightData:
    flights = {}
    FILE_NAME = "Project\\DataLayer\\flight.csv"

    def __init__(self):
        self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.FILE_NAME, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skps the header row
            for row in reader:
                flight_id = row[0]
                flight_info = row[1:]
                flight = Flight.from_row(flight_id, flight_info)
                self.flights[flight_id] = flight

    def save_data_to_file(self):
        with open(self.FILE_NAME, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for flight in self.flights.values():
                writer.writerow(flight.serialize())

    def create_flight(self, flight: Flight):
        self.flights[flight.flight_id] = flight
        self.save_data_to_file()

    def get_flight_by_id(self, flight_id):
        return self.flights.get(flight_id, None)

    def get_flight_list(self):
        return list(self.flights.values())
    
    def get_employees_not_working(self, day):
        day = datetime.strptime(day, '%d/%m/%Y')
        with open(self.FILE_NAME, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            flights = list(reader)

        working_employees = set()
        for flight in flights:
            if 'DepartureDate' in flight:
                flight_day = datetime.strptime(flight['DepartureDate'], '%d/%m/%Y')
                if flight_day.date() == day.date():
                    working_employees.add(flight['CaptainSSN'])
                    working_employees.add(flight['PilotSSN'])
                    working_employees.add(flight['Flight_service_managerSSN'])
                    working_employees.add(flight['Flight_AttendantSSN'])

        with open('Project\\DataLayer\\employee.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            employees = list(reader)

        employees_not_working = [employee for employee in employees if employee['SSN'] not in working_employees]
        for employee in employees_not_working:
            print(f"Name: {employee['Name']}, SSN: {employee['SSN']}, Rank: {employee['Rank']}")