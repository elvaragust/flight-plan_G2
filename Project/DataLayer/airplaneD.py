import csv
from airplaneM import Airplanes

class AirplaneData:
    airplanes = {}
    FILE_NAME = "airplanes.csv"

    def __init__(self):
        self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.FILE_NAME, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skips the header row
            for row in reader:
                name, model, manufacturer, seats = row
                airplane = Airplanes(name, model, manufacturer, int(seats))
                self.airplanes[airplane.name] = airplane

    def save_data_to_file(self):
        with open(self.FILE_NAME, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for airplane in self.airplanes.values():
                writer.writerow(airplane.serialize())

    def create_airplane(self, airplane: Airplanes):
        self.airplanes[airplane.name] = airplane
        self.save_data_to_file()

    def get_airplane_by_name(self, airplane_name):
        return self.airplanes.get(airplane_name, None)

    def get_airplane_list(self):
        return list(self.airplanes.values())