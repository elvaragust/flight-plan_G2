from enum import Enum

class Rank(Enum):
    PILOT = "pilot"
    ASSISTANT_PILOT = "assistant_pilot"
    HEAD_FLIGHT_ATTENDANT = "head_flight_attendant"
    FLIGHT_ATTENDANT = "flight_attendant"

class Employees:
    def __init__(self, social_security: str, name: str, rank: Rank, email: str, phone: str, landline: str, license: str, address: str):
        self.social_security = social_security
        self.name = name
        self.rank = rank
        self.email = email
        self.phone = phone
        self.landline = landline
        self.license = license
        self.address = address

def serialize(self) -> list:
    return [self.social_security, self.name, self.rank, self.email, self.phone, self.landline, self.license, self.address]