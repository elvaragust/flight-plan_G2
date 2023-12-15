import csv
from models.flightM import Flight

class FlightData:
    flights = {}
    FILE_NAME = "flight.csv"

    def __init__(self):
        self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.FILE_NAME, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skps the header row
            for row in reader:
                flight_id = row[0]
                flight_info = row[1:]
                flight = Flight.from_row(flight_id, flight_info)
                self.flights[flight_id] = flight

    def save_data_to_file(self):
        with open(self.FILE_NAME, 'a', newline='') as csvfile:
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