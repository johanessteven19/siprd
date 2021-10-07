from django.test import TestCase
from rest_framework.test import APIClient
from .models import User
from django.urls import resolve

# NOTE: These tests suck, feel free to refactor.
class SIPRDUnitTest(TestCase):
	global Register_URL, Edit_URL, Delete_URL, Email, Full_Name
	Register_URL= "/api/register"
	Edit_URL = "/api/edit/"
	Delete_URL = "/api/delete/"
	Email = "test.user@example.com"
	Full_Name = "Test User"

	def setUp(self):
		self.client = APIClient()

		self.tester = User.objects.create(
				username = 'tester',
				email = Email,
				password = 'test',
				full_name = Full_Name,
				university = 'UI',
				field_of_study = 'Art',
				position = 'Lektor',
				role = 'Admin'
		)

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

	
	## == Edit Data Tests == ##
	def test_edit_user_data_returns_HTTP_OK(self):
		response = self.client.put(
			Edit_URL + "tester",
			{
				'username': 'tester',
				'email': Email,
				'password': 'test',
				'full_name': Full_Name,
				'university': 'UGM',
				'expertise': 'Art',
				'position': 'Lektor',
				'role': 'Admin'
			},
			format='json'
		)

		self.assertEqual(response.status_code, 200)

	def test_edit_user_data_user_not_found_returns_HTTP_NOT_FOUND(self):
		response = self.client.put(
			Edit_URL + "random",
			{
				'username': 'test',
				'email': Email,
				'password': 'test',
				'full_name': Full_Name,
				'university': 'UGM',
				'expertise': 'Art',
				'position': 'Lektor',
				'role': 'Admin'
			},
			format='json'
		)

		self.assertEqual(response.status_code, 404)

	def test_edit_user_data_incomplete_request_returns_HTTP_BAD_REQUEST(self):
		response = self.client.put(
			Edit_URL + "tester",
			{
				'university': 'UGM',
			},
			format='json'
		)

		self.assertEqual(response.status_code, 400)
	
	## == Delete Dosen Tests == ##
	def test_delete_user_data_returns_HTTP_NO_CONTENT(self):
		response = self.client.delete(
			Delete_URL + "tester"
		)

		self.assertEqual(response.status_code, 204)

	def test_delete_user_data_not_found_returns_HTTP_NOT_FOUND(self):
		response = self.client.delete(
			Delete_URL + "123132132213"
		)

		self.assertEqual(response.status_code, 404)
