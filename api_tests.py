import requests
import json
import unittest
from timetabling_api import *

class StudentsTest(unittest.TestCase):
	"""To test the GET function on the students class"""
	def test_get_request(self):
		"""Does it get the required data"""
		student_details = 
	
	
	
	def do_get(self, suffix):
		return requests.get(self.data + suffix).json()
	def get(self):
		return self.do_get('data')


class TestFunctions(StudentsTest):
	def do_get(self, suffix):
		self.request_log.append(suffix)
		return self.send_result

	def test_data(self):
		student = TestFunctions(send_result='par')
		assert_equal(student.get(), 'par')
		assert_contains(student.request_log, 'data')