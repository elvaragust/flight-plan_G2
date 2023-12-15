import csv
from models.flightM import Flight

class FlightData:
    flights = {}
    FILE_NAME = "dataLayer\\flight.csv"

    def __init__(self):
        pass

    def get_all_flights(self):
        """ returns a list of all flights
        
        args: None
        
        returns: list of all flights
        
        """
        flight_list = []
        with open(self.FILE_NAME, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                flight_list.append(row)
        return flight_list

    def save_data_to_file(self):
        """ saves the flight list to the csv fiel
        
        args: None
        
        returns: None
        
        """
        with open(self.FILE_NAME, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for flight in self.flights.values():
                writer.writerow(flight.serialize())

    def create_flight(self, flight: Flight):
        """ creates an flight and saves it to the csv file
        
        args: flight object
        
        returns: None
        
        """
        self.flights[flight.flight_id] = flight
        self.save_data_to_file()

    def get_flight_by_id(self, flight_id):
        """ finds an flight by id and returns it
        
        args: id of the flight
        
        returns: flight object
        
        """
        return self.flights.get(flight_id, None)


    
