from city_functions import city_country_name
import unittest

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        """Test the output of the city_country_name function"""
        string_output = city_country_name('nairobi', 'kenya')
        self.assertEqual(string_output, 'Nairobi Kenya')

    def test_city_country_population(self):
        """Test the output when a population is added"""
        string_output = city_country_name('nairobi', 'kenya', '4.3million')
        self.assertEqual(string_output, 'Nairobi Kenya, population: 4.3million')


unittest.main()