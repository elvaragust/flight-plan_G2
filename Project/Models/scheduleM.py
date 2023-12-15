class ScheduleModel:
    def __init__(self, flight_number, departure_date, departure_time, arriving_date, arriving_time, name, destination, gate):
        self.flight_number = flight_number
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.arriving_date = arriving_date
        self.arriving_time = arriving_time
        self.name = name
        self.destination = destination
        self.gate = gate