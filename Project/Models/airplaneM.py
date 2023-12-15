
class Airplanes:
    def __init__(self, name: str, model: str, manufacturer: str, seats: int):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.seats = seats

def serialize(self) -> list:
    return [self.name, self.model, self.manufacturer, self.seats]