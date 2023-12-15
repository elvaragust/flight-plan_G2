class Voyage:
    def __init__(self, voyage_id: int, destination: str, first_flight_date: str, last_flight_date: str):
        self.voyage_id = voyage_id
        self.destination = destination
        self.first_flight_date = first_flight_date
        self.last_flight_date = last_flight_date

    def serialize(self) -> list:
        return [self.voyage_id, self.destination, self.first_flight_date, self.last_flight_date]