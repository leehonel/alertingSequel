""" A unit test verifies that one specific aspect of a function's behavior is correct. 
    A test case is a collection of unit tests used to prove a function works okay. 
    To write a test case, import the unittest module and the function to be tested. 
    Then create a class that inherits from unittest.TestCase, and write a series of methods that test different aspects
    of the function's behavior. 
"""
import unittest
#first import the function to be tested
from name_function import get_formatted_name

#create a class containing a series of unit tests
#method names should start with 'test' so that they can run automatically when the test file is run
class NameTestCase(unittest.TestCase):
    """Tests for the name_function.py."""
    def test_first_last_name(self):
        """Do names like 'Da Capo' work?"""
        formatted_name = get_formatted_name('da', 'capo')
        #the assert method verifies that the recieved result is indeed the one that was expected. 
        self.assertEqual(formatted_name, 'Da Capo')
    def test_first_last_middle_name(self):
        """Do names like 'Elvis Leon Okeda' work?"""
        formatted_name = get_formatted_name('elvis', 'okeda', 'leon')
        self.assertEqual(formatted_name, 'Elvis Leon Okeda')

unittest.main() #this tells python to run the tests in this file
