from django.test import TestCase
from rest_framework.test import APIClient
from .models import KaryaIlmiah, User
from django.urls import resolve

# NOTE: These tests suck, feel free to refactor.
class SIPRDUnitTest(TestCase):
	register_url = "/api/register"
	login_url = "/api/token/"
	manage_users_url = "/api/manage-users/"
	manage_review_url = "/api/manage-reviews/"
	karil_summary_url = "/api/get-karil-summary/"
	header_prefix = "Bearer "
	email = "test.user@example.com"
	full_name = "Test User"
	username = "tester"
	password = "test"
	dosen_username = "dosen"
	dosen_fullname = "dosen"
	reviewer_username = "reviewer"
	reviewer_fullname = "reviewer_name"
	random_name = "no one"

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

		self.dosen = User.objects.create_user(
				username = self.dosen_username,
				email = self.email,
				password = self.password,
				full_name = self.dosen_fullname,
				university = 'UI',
				field_of_study = 'Art',
				position = 'Lektor',
				role = 'Dosen'
		)

		self.reviewer = User.objects.create_user(
				username = self.reviewer_username,
				email = self.email,
				password = self.password,
				full_name = self.reviewer_fullname,
				university = 'UI',
				field_of_study = 'Art',
				position = 'Lektor',
				role = 'Reviewer'
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
	
	## Use this instead for tests that require 'Dosen' role exclusively
	def LoginDosen(self):
		response = self.client.post(
			self.login_url,
			{
				'username': self.dosen_username,
				'password': self.password
			}, format='json')

		_, access = response.json().values()
		return access

	## Use this instead for tests that require 'Reviewer' role exclusively
	def LoginReviewer(self):
		response = self.client.post(
			self.login_url,
			{
				'username': self.reviewer_username,
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

	# def test_edit_user_data_incomplete_request_returns_HTTP_BAD_REQUEST(self):
	# 	access = self.login()

	# 	self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + access)
	# 	response = self.client.put(
	# 		self.manage_users_url,
	# 		{
	# 			'university': 'UGM'
	# 		},
	# 		format='json'
	# 	)

	# 	self.assertEqual(response.status_code, 400)
	
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

	def test_get_karil_not_created_returns_HTTP_NO_CONTENT(self):
		access = self.login()

		self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + access)
		response = self.client.get(self.karil_summary_url)
		self.assertEqual(response.status_code, 204)
	
	def test_get_karil_based_on_username(self):
		access = self.login()

		self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + access)
		self.client.post(
			self.manage_review_url,
			{
				'pemilik': self.full_name,
				'judul': 'test judul',
				'journal_data': 'test journal',
				'link_origin': 'www.google.com',
				'link_repo': 'www.google.com',
				'link_indexer': 'www.google.com',
				'link_simcheck': 'www.google.com',
				'link_correspondence': 'www.google.com',
				'indexer': 'test indexer',
				'category': 'Buku',
				'promotion': 'Lektor',
				'status': 'Not Reviewed Yet',
			},
			format='json')
		
		response = self.client.get(self.karil_summary_url)
		self.assertEqual(response.status_code, 200)


	def test_create_review_form_returns_HTTP_OK(self):

		access = self.LoginDosen()
		self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + access)

		response = self.client.post(
			self.manage_review_url,
			{
				'pemilik': self.dosen_username,
				'judul': 'test judul',
				'journal_data': 'test journal',
				'link_origin': 'www.google.com',
				'link_repo': 'www.google.com',
				'link_indexer': 'www.google.com',
				'link_simcheck': 'www.google.com',
				'link_correspondence': 'www.google.com',
				'indexer': 'test indexer',
				'category': 'Buku',
				'promotion': 'Lektor',
				'status': 'Not Reviewed Yet',
			},
			format='json')
		
		self.assertEqual(response.status_code, 201)

	def test_create_review_form_as_reviewer_returns_HTTP_UNAUTHORIZED(self):

		access = self.LoginReviewer()
		self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + access)

		response = self.client.post(
			self.manage_review_url,
			{
				'pemilik': self.full_name,
				'judul': 'test judul',
				'journal_data': 'test journal',
				'link_origin': 'www.google.com',
				'link_repo': 'www.google.com',
				'link_indexer': 'www.google.com',
				'link_simcheck': 'www.google.com',
				'link_correspondence': 'www.google.com',
				'indexer': 'test indexer',
				'category': 'Buku',
				'promotion': 'Lektor',
				'status': 'Not Reviewed Yet',
			},
			format='json')
		
		self.assertEqual(response.status_code, 401)

	def test_create_review_form_incomplete_request_returns_HTTP_BAD_REQUEST(self):

		access = self.LoginDosen()
		self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + access)

		response = self.client.post(
			self.manage_review_url,
			{
				'pemilik': self.dosen_username,
				'judul': 'test judul',
			},
			format='json')
		
		self.assertEqual(response.status_code, 400)

	def test_delete_review_form_returns_HTTP_OK(self):

		access = self.LoginDosen()
		self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + access)

		karil = KaryaIlmiah.objects.create(
				pemilik = self.dosen,
				judul = 'test judul',
				journal_data = 'test journal',
				link_origin = 'www.google.com',
				link_repo = 'www.google.com',
				link_indexer = 'www.google.com',
				link_simcheck = 'www.google.com',
				link_correspondence = 'www.google.com',
				indexer = 'test indexer',
				category = 'Buku',
				promotion = 'Lektor',
				status = 'Not Reviewed Yet',
		)

		karil_id = karil.pk
		response = self.client.delete(
				self.manage_review_url,
				{
					'karil_id': karil_id,
					'pemilik': self.dosen_username,
					'judul': 'test judul',
					'journal_data': 'test journal',
					'link_origin': 'www.google.com',
					'link_repo': 'www.google.com',
					'link_indexer': 'www.google.com',
					'link_simcheck': 'www.google.com',
					'link_correspondence': 'www.google.com',
					'indexer': 'test indexer',
					'category': 'Buku',
					'promotion': 'Lektor',
					'status': 'Not Reviewed Yet',
				},
				format='json')

		self.assertEqual(response.status_code, 200)

	def test_delete_review_form_not_exist_returns_HTTP_NOT_FOUND(self):

		access = self.LoginDosen()
		self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + access)

		karil = KaryaIlmiah.objects.create(
				pemilik = self.dosen,
				judul = 'test judul',
				journal_data = 'test journal',
				link_origin = 'www.google.com',
				link_repo = 'www.google.com',
				link_indexer = 'www.google.com',
				link_simcheck = 'www.google.com',
				link_correspondence = 'www.google.com',
				indexer = 'test indexer',
				category = 'Buku',
				promotion = 'Lektor',
				status = 'Not Reviewed Yet',
		)

		response = self.client.delete(
				self.manage_review_url,
				{
					'karil_id': 999,
					'pemilik': self.dosen_username,
					'judul': 'test judul',
					'journal_data': 'test journal',
					'link_origin': 'www.google.com',
					'link_repo': 'www.google.com',
					'link_indexer': 'www.google.com',
					'link_simcheck': 'www.google.com',
					'link_correspondence': 'www.google.com',
					'indexer': 'test indexer',
					'category': 'Buku',
					'promotion': 'Lektor',
					'status': 'Not Reviewed Yet',
				},
				format='json')

		self.assertEqual(response.status_code, 404)
	
	def test_delete_review_form_as_non_dosen_returns_HTTP_UNAUTHORIZED(self):

		access = self.login()
		self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + access)

		karil = KaryaIlmiah.objects.create(
				pemilik = self.tester,
				judul = 'test judul',
				journal_data = 'test journal',
				link_origin = 'www.google.com',
				link_repo = 'www.google.com',
				link_indexer = 'www.google.com',
				link_simcheck = 'www.google.com',
				link_correspondence = 'www.google.com',
				indexer = 'test indexer',
				category = 'Buku',
				promotion = 'Lektor',
				status = 'Not Reviewed Yet',
		)

		karil_id = karil.pk
		response = self.client.delete(
				self.manage_review_url,
				{
					'karil_id': karil_id,
					'pemilik': self.dosen_username,
					'judul': 'test judul',
					'journal_data': 'test journal',
					'link_origin': 'www.google.com',
					'link_repo': 'www.google.com',
					'link_indexer': 'www.google.com',
					'link_simcheck': 'www.google.com',
					'link_correspondence': 'www.google.com',
					'indexer': 'test indexer',
					'category': 'Buku',
					'promotion': 'Lektor',
					'status': 'Not Reviewed Yet',
				},
				format='json')

		self.assertEqual(response.status_code, 401)
