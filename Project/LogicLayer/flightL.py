class FlightL():
    
    def __init__(self, flightNr, depDate, depTime, arrDate, arrTime, airplane, destination):
        self.flightNr = flightNr
        self.depDate = depDate
        self.depTime = depTime
        self.arrDate = arrDate
        self.arrTime = arrTime
        self.airplane = airplane
        self.destination = destination
        self.flight = {}
        
        
    def create_flight(self):
        self.flight[self.flightNr] = [self.depDate, self.depTime, self.arrDate, self.arrDate, self.airplane, self.destination]
    
    def edit_flight(self):
        pass
    
    def assign_staff(self):
        pass
    
    def get_flight_info(self):
        pass
    