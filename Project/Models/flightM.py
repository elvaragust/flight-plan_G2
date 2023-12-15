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

    def serialize(self) -> list:
        return [
            self.flight_id,
            self.voyage_id,
            self.flight_number,
            self.departure_date,
            self.departure_time,
            self.arriving_date,
            self.arriving_time,
            self.from_destination,
            self.to_destination,
            self.airplane_name,
            self.captain_ssn,
            self.pilot_ssn,
            self.flight_service_manager_ssn,
            self.flight_attendant_ssn
        ]
    @classmethod
    def from_row(cls, flight_id, flight_info):
        return cls(flight_id, *flight_info)
