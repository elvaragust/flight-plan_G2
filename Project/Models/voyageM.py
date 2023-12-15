class Voyage:
    def __init__(self, voyage_id: int, destination: str, first_flight_date: str, last_flight_date: str):
        self.voyage_id = voyage_id
        self.destination = destination
        self.first_flight_date = first_flight_date
        self.last_flight_date = last_flight_date

    def serialize(self) -> dict:
        return {
            'voyage_id': self.voyage_id,
            'destination': self.destination,
            'first_flight_date': self.first_flight_date,
            'last_flight_date': self.last_flight_date
        }
    
    @classmethod
    def from_row(cls, voyage_id, voyage_info):
        return cls(voyage_id, *voyage_info)