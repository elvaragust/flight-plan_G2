import csv
from models.airplaneM import Airplanes

class AirplaneData:
    FILE_NAME = "dataLayer/airplane.csv"
    def __init__(self):
        self.airplanes = {}

    def load_data_from_file(self):
        with open(self.FILE_NAME, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header
            for row in reader:
                if row:  # Skip empty lines
                    name, model, manufacturer, seats = row
                    airplane = Airplanes(name, model, manufacturer, int(seats))
                    self.airplanes[name] = airplane  # Store the airplane in the airplanes dictionary
                    
    def save_data_to_file(self):
        with open(self.FILE_NAME, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for airplane in self.airplanes.values():
                writer.writerow([airplane.name, airplane.model, airplane.manufacturer, airplane.seats])
                
                
                
    def create_airplane(self, airplane: Airplanes):
        self.airplanes[airplane.name] = airplane
        self.save_data_to_file()

    def get_airplane_by_name(self, airplane_name):
        return self.airplanes.get(airplane_name, None)

    def get_airplane_list(self):
        return list(self.airplanes.values())
    
