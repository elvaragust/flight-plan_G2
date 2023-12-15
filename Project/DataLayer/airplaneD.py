import csv
from models.airplaneM import Airplanes

class AirplaneData:
    airplanes = {}
    FILE_NAME = "dataLayer\\airplane.csv"
    
    def __init__(self):
        pass

    def get_all_airplanes(self):
        airplane_list = []
        with open(self.FILE_NAME, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                airplane_list.append(row)  # append the row directly
        return airplane_list
            
    def save_data_to_file(self):
        with open(self.FILE_NAME, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for airplane in self.airplanes.values():
                writer.writerow(airplane.serialize())
                
    def create_airplane(self, airplane: Airplanes):
        self.airplanes[airplane.name] = airplane
        self.save_data_to_file()

    def get_airplane_by_name(self, name):
        return self.airplanes.get(name, None)


    
