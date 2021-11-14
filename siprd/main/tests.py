from django.test import TestCase
from rest_framework.test import APIClient
from .models import User
from django.urls import resolve

# NOTE: These tests suck, feel free to refactor.
class SIPRDUnitTest(TestCase):
	register_url = "/api/register"
	login_url = "/api/token/"
	manage_users_url = "/api/manage-users/"
	header_prefix = "Bearer "
	email = "test.user@example.com"
	full_name = "Test User"
	username = "tester"
	password = "test"

	def setUp(self):
		self.client = APIClient()

		self.tester = User.objects.create_user(
				username = self.username,
				email = self.email,
				password = self.password,
				full_name = self.full_name,
				university = 'UI',
				field_of_study = 'Art',
				position = 'Lektor',
				role = 'Admin'
		)

	def login(self):
		response = self.client.post(
			self.login_url,
			{
				'username': self.username,
				'password': self.password
			}, format='json')

		_, access = response.json().values()
		return access

	def test_ping_url_exists(self):
		response = self.client.get('/ping')
		self.assertEqual(response.status_code, 200)

	def test_ping_can_return_JSON_data(self):
		response = self.client.get('/ping')
		self.assertEqual(response.json().get('foo'), 'bar')

	
	def test_api_register_new_user_returns_HTTP_Status_201_CREATED(self):
		response = self.client.post(
			self.register_url,
			{
				'username': 'test',
				'email': self.email,
				'password': 'test',
				'full_name': self.full_name,
				'university': 'UI',
				'expertise': 'Art',
				'position': 'Lektor',
				'role': 'Admin'
			},
			format='json')
		self.assertEqual(response.status_code, 201)

	def test_api_register_new_user_incomplete_returns_HTTP_Status_400_BAD_REQUEST(self):
		response = self.client.post(
			self.register_url,
			{
				'username': 'test'
			})
		self.assertEqual(response.status_code, 400)

	def test_login_new_user_returns_HTTP_Status_OK(self):
		self.client.post(
			self.register_url,
			{
				'username': 'test',
				'email': self.email,
				'password': 'test',
				'full_name': self.full_name,
				'university': 'UI',
				'expertise': 'Art',
				'position': 'Lektor',
				'role': 'Admin'
			},
			format='json')

		response = self.client.post(
			self.login_url,
			{
				'username': 'test',
				'password': 'test'
			}, format='json')

		self.assertEqual(response.status_code, 200)
		
	def test_login_new_user_returns_JWT_token_pair(self):
		self.client.post(
			self.register_url,
			{
				'username': 'test',
				'email': self.email,
				'password': 'test',
				'full_name': self.full_name,
				'university': 'UI',
				'expertise': 'Art',
				'position': 'Lektor',
				'role': 'Admin'
			},
			format='json')

		response = self.client.post(
			self.login_url,
			{
				'username': 'test',
				'password': 'test'
			}, format='json')

		access, refresh = response.json().values()
		self.assertIsNotNone(access)
		self.assertIsNotNone(refresh)

	
	## == Edit Data Tests == ##
	def test_edit_user_data_returns_HTTP_OK(self):
		access = self.login()

		self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + access)
		response = self.client.put(
			self.manage_users_url,
			{
				'username': self.username,
				'email': self.email,
				'password': self.password,
				'full_name': self.full_name,
				'university': 'UGM',
				'expertise': 'Art',
				'position': 'Lektor',
				'role': 'Admin'
			},
			format='json'
		)

		self.assertEqual(response.status_code, 200)

	def test_edit_user_data_user_not_found_returns_HTTP_NOT_FOUND(self):
		access = self.login()

		self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + access)
		response = self.client.put(
			self.manage_users_url,
			{
				'username': 'doesnotexist',
				'email': self.email,
				'password': 'test',
				'full_name': self.full_name,
				'university': 'UGM',
				'expertise': 'Art',
				'position': 'Lektor',
				'role': 'Admin'
			},
			format='json'
		)

		self.assertEqual(response.status_code, 404)
	
	## == Delete Dosen Tests == ##
	def test_successful_delete_user_data_returns_HTTP_OK(self):
		access = self.login()

		self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + access)
		response = self.client.delete(
			self.manage_users_url,
			{
				'username': self.username
			}
		)

		self.assertEqual(response.status_code, 200)

	def test_delete_user_data_not_found_returns_HTTP_NOT_FOUND(self):
		access = self.login()

		self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + access)
		response = self.client.delete(
			self.manage_users_url,
			{
				'username': 'doesnotexist'
			}
		)

		self.assertEqual(response.status_code, 404)
