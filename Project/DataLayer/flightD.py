import csv
from models.flightM import Flight

class FlightData:
    flights = {}
    FILE_NAME = "dataLayer\\flight.csv"

    def __init__(self):
        pass

    def get_all_flights(self):
        flight_list = []
        with open(self.FILE_NAME, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                flight_list.append(row)
        return flight_list

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


    
