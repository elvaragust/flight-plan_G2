
class Airplanes:
    def __init__(self, name: str, model: str, manufacturer: str, seats: int):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.seats = seats

    def serialize(self) -> dict:
        return {
            'name': self.name,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'seats': self.seats
        }