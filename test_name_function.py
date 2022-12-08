import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""тесты для name_function.py"""
	
	def test_first_last_name(self):
		"""имена вида janis joplin работают правильно?"""
		formatted_name=get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin')
	
	def test_first_last_midle_name(self):
		"""Работают ли такие имена, как 'Wolfgana Amadeus Mazart'?"""
		formatted_name=get_formatted_name('wolfgang','mozart','amadeus')
		self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

unittest.main()
