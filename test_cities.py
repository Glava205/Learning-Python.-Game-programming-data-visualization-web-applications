import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
	def test_city_country(self):
		ci_co=city_country('santiago','chile')
		self.assertEqual(ci_co,'Santiago, Chile')
	
	def test_city_country_population(self):
		ci_co_po=city_country('santiago','chile','5000000')
		self.assertEqual(ci_co_po,'Santiago, Chile- population 5000000.')

unittest.main()
