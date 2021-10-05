from django.test import TestCase
from rest_framework.test import APIClient
from .models import User
from django.urls import resolve

# NOTE: These tests suck, feel free to refactor.
class SIPRDUnitTest(TestCase):
	global Register_URL, Email, Full_Name
	Register_URL= "/api/register"
	Email = "test.user@example.com"
	Full_Name = "Test User"

	def setUp(self):
		self.client = APIClient()

	def test_ping_url_exists(self):
		response = self.client.get('/ping')
		self.assertEqual(response.status_code, 200)

	def test_ping_can_return_JSON_data(self):
		response = self.client.get('/ping')
		self.assertEqual(response.json().get('foo'), 'bar')

	
	def test_api_register_new_user_returns_HTTP_Status_201_CREATED(self):
		response = self.client.post(
			Register_URL,
			{
				'username': 'test',
				'email': Email,
				'password': 'test',
				'full_name': Full_Name,
				'university': 'UI',
				'expertise': 'Art',
				'position': 'Lektor',
				'role': 'Admin'
			},
			format='json')
		self.assertEqual(response.status_code, 201)

	def test_api_register_new_user_incomplete_returns_HTTP_Status_400_BAD_REQUEST(self):
		response = self.client.post(
			Register_URL,
			{
				'username': 'test'
			})
		self.assertEqual(response.status_code, 400)

	def test_login_new_user_returns_HTTP_Status_OK(self):
		self.client.post(
			Register_URL,
			{
				'username': 'test',
				'email': Email,
				'password': 'test',
				'full_name': Full_Name,
				'university': 'UI',
				'expertise': 'Art',
				'position': 'Lektor',
				'role': 'Admin'
			},
			format='json')

		response = self.client.post(
			'/api/token/',
			{
				'username': 'test',
				'password': 'test'
			}, format='json')

		self.assertEqual(response.status_code, 200)
		
	def test_login_new_user_returns_JWT_token_pair(self):
		self.client.post(
			Register_URL,
			{
				'username': 'test',
				'email': Email,
				'password': 'test',
				'full_name': Full_Name,
				'university': 'UI',
				'expertise': 'Art',
				'position': 'Lektor',
				'role': 'Admin'
			},
			format='json')

		response = self.client.post(
			'/api/token/',
			{
				'username': 'test',
				'password': 'test'
			}, format='json')

		access, refresh = response.json().values()
		self.assertIsNotNone(access)
		self.assertIsNotNone(refresh)