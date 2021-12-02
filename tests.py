
import unittest
import requests
from timetabling_api import Students, Lessons

class StudentDetailsTestCase(unittest.TestCase):
	#test for get StudentDetails
	def test_get_data(self):
		#test get data

		get_data = 'data'
		self.assertEqual(get_data, 'data')

	def test_post_data(self):
		#test for post data
		post_data = 'data'
		self.assertEqual(post_data, 'data')

class StudentLessonsTestCase(unittest.TestCase):
	#test for course lessons
	def test_get_lessons(self):
		get_lessons = 'data'
		self.assertEqual(get_lessons, 'data')
class StudentEventsTestCase(unittest.TestCase):
	#test for course lessons
	def test_get_events(self):
		get_events = 'data'
		self.assertEqual(get_events, 'data')

if __name__ == '__main__':
	unittest.main()

