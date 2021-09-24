from django.test import TestCase,Client
from django.urls import resolve
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# import time

class SIPRDUnitTest(TestCase):
	def setUp(self):
		self.client = Client()

	def test_ping_url_exists(self):
		response = self.client.get('/ping')
		self.assertEqual(response.status_code, 200)
    
	def register_url_exists(self):
		response = self.client.get('/register')
		self.assertEqual(response.status_code, 200)

	def login_url_exists(self):
		response = self.client.get('/login')
		self.assertEqual(response.status_code, 200)

	def register_new_user_returns_HTTP_Status_OK(self):
		response = self.client.post('/register',{'username': 'test', 'email': 'test@gmil.com', 'password1': 'test', 'password2': 'test',
        'university': 'UI', 'expertise': 'good', 'position': 'Lecturer', 'role': 'Admin'})
		self.assertEqual(response.status_code, 200)

	def register_new_user_incomplete_returns_HTTP_Status_NotFound(self):
		response = self.client.post('/register',{'username': 'test','password1': 'test', 'password2': 'test', 'expertise': 'good',
        'position': 'Lecturer', 'role': 'Admin'})
		self.assertEqual(response.status_code, 404)

	def login_new_user_returns_HTTP_Status_OK(self):
		response = self.client.post('/register',{'username': 'test', 'password': 'test'})
		self.assertEqual(response.status_code, 200)