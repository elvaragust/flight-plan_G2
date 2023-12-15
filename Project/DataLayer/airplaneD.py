import csv
from models.airplaneM import Airplanes

class AirplaneData:
    airplanes = {}
    FILE_NAME = "dataLayer\\airplane.csv"
    
    def __init__(self):
        pass

    def get_all_airplanes(self):
        """ returns a list of all airplanes
        
        args: None
        
        returns: list of all airplanes
        
        """
        airplane_list = []
        with open(self.FILE_NAME, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                airplane_list.append(row)  # append the row directly
        return airplane_list
    
            
    def save_data_to_file(self):
        """ saves the airplane list to the csv file
        
        args: None
        
        returns: None
        
        """
        with open(self.FILE_NAME, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for airplane in self.airplanes.values():
                writer.writerow(airplane.serialize())
                
    def create_airplane(self, airplane: Airplanes):
        """ creates an airplane and saves it to the csv file
        
        args: airplane object
        
        returns: None
        
        """
        self.airplanes[airplane.name] = airplane
        self.save_data_to_file()

    def get_airplane_by_name(self, name):
        """ finds an airplane by name and returns it
        
        args: name of the airplane
        
        returns: airplane object
        
        """
        return self.airplanes.get(name, None)


    
