import unittest
from dataLayer.airplaneD import AirplaneData
from models.airplaneM import Airplanes

class TestAirplaneData(unittest.TestCase):
    def setUp(self):
        self.airplane_data = AirplaneData()
        self.airplane_data.load_data_from_file()

    def test_create_and_get_airplanes(self):
        # Create an airplane
        airplane = Airplanes('Test Plane', 'Model 1', 'Manufacturer 1', 100)
        self.airplane_data.create_airplane(airplane)

        # Test getting airplane by name
        retrieved_airplane = self.airplane_data.get_airplane_by_name('Test Plane')
        print(f"Retrieved airplane: {retrieved_airplane}")
        self.assertEqual(retrieved_airplane, airplane)

    def test_get_airplane_list(self):
        # Test getting all airplanes
        retrieved_airplanes = self.airplane_data.get_airplane_list()
        print("Retrieved airplanes:")
        for airplane in retrieved_airplanes:
            print(airplane)
        self.assertIsInstance(retrieved_airplanes, list)
        self.assertTrue(all(isinstance(plane, Airplanes) for plane in retrieved_airplanes))

if __name__ == '__main__':
    unittest.main()