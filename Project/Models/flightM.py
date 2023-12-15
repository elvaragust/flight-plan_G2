class Flight:
    def __init__(self, flight_id: int, voyage_id: int, flight_number: str, departure_date: str, departure_time: int, arriving_date: str, arriving_time: int, from_destination: str, to_destination: str, airplane_name: str, captain_ssn: str, pilot_ssn: str, flight_service_manager_ssn: str, flight_attendant_ssn: str):
        self.flight_id = flight_id
        self.voyage_id = voyage_id
        self.flight_number = flight_number
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.arriving_date = arriving_date
        self.arriving_time = arriving_time
        self.from_destination = from_destination
        self.to_destination = to_destination
        self.airplane_name = airplane_name
        self.captain_ssn = captain_ssn
        self.pilot_ssn = pilot_ssn
        self.flight_service_manager_ssn = flight_service_manager_ssn
        self.flight_attendant_ssn = flight_attendant_ssn

    def serialize(self) -> dict:
        return {
            'flight_id': self.flight_id,
            'voyage_id': self.voyage_id,
            'flight_number': self.flight_number,
            'departure_date': self.departure_date,
            'departure_time': self.departure_time,
            'arriving_date': self.arriving_date,
            'arriving_time': self.arriving_time,
            'from_destination': self.from_destination,
            'to_destination': self.to_destination,
            'airplane_name': self.airplane_name,
            'captain_ssn': self.captain_ssn,
            'pilot_ssn': self.pilot_ssn,
            'flight_service_manager_ssn': self.flight_service_manager_ssn,
            'flight_attendant_ssn': self.flight_attendant_ssn
        }
    
    @classmethod
    def from_row(cls, flight_id, flight_info):
        return cls(flight_id, *flight_info)