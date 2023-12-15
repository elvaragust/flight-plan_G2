import unittest
from dataLayer.airplaneD import AirplaneData
from models.airplaneM import Airplanes

class TestAirplaneData(unittest.TestCase):
    def setUp(self):
        self.airplane_data = AirplaneData()

    def test_create_airplane(self):
        airplane = Airplanes('Test Plane', 'Model 1', 'Manufacturer 1', 100)
        self.airplane_data.create_airplane(airplane)
        self.assertEqual(self.airplane_data.get_airplane_by_name('Test Plane'), airplane)

    def test_get_airplane_by_name(self):
        airplane = Airplanes('Test Plane', 'Model 1', 'Manufacturer 1', 100)
        self.airplane_data.create_airplane(airplane)
        self.assertEqual(self.airplane_data.get_airplane_by_name('Test Plane'), airplane)

if __name__ == '__main__':
    unittest.main()