
class Airplanes:
    def __init__(self, name, model, manufacturer, seats):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.seats = seats

    def __str__(self):
        return f"{self.name},{self.model},{self.manufacturer},{self.seats}"