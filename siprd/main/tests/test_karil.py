from django.test import TestCase
from rest_framework.test import APIClient
from ..models import User

class TestKaril(TestCase):
	header_prefix = "Bearer "
	email = "test.user@example.com"
	full_name = "Karil Tester"
	username = "kariltester"
	not_pass = "supersecure"
	access = ""
	karil_url = "/api/manage-reviews/"
	review_url = "/api/manage-karil-reviews"
	assignment_url = "api/assign-reviewer/"
	reviewer_username = "test_reviewer"
	reviewer_full_name = "Test Reviewer"

	def setUp(self):
		self.client = APIClient()

		self.tester = User.objects.create_user(
			username = self.username,
			email = self.email,
			password = self.not_pass,
			full_name = self.full_name,
			university = 'UI',
			field_of_study = 'Art',
			position = 'Lektor',
			role = 'Admin'
		)

		self.reviewer = User.objects.create_user(
			username = self.reviewer_username,
			email = self.email,
			password = self.not_pass,
			full_name = self.reviewer_full_name,
			university = 'UI',
			field_of_study = 'Science',
			position = 'Guru Besar/Professor',
			role = 'Reviewer'
		)

		response = self.client.post(
			"/api/token/",
			{
				'username': self.username,
				'password': self.not_pass
			}, format='json')

		_, self.access = response.json().values()
	
	# Karil creation tests
	def test_create_valid_karil_returns_HTTP_CREATED(self):
		self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + self.access)
		response = self.client.post(
			self.karil_url,
			{
				"pemilik": self.full_name,
				"judul": "Lorem Ipsum: Dolor sit amet",
				"link_origin": "www.origin.com",
				"category": "Buku",
				"promotion": "Lektor",
				"status": "Not Reviewed Yet",
			}, format='json'
		)

		self.assertEqual(response.status_code, 201)

	def test_create_invalid_karil_returns_HTTP_BAD_REQUEST(self):
		self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + self.access)
		response = self.client.post(
			self.karil_url,
			{
				"pemilik": "User Who Does Not Exist",
				"judul": "Invalid",
				"link_origin": "www.origin.com",
				"category": "Buku",
				"promotion": "Lektor",
				"status": "Not Reviewed Yet",
			}
		)

		self.assertEqual(response.status_code, 400)

	def test_assignment_to_nonexistent_karil_returns_NOT_FOUND(self):
		self.client.credentials(HTTP_AUTHORIZATION=self.header_prefix + self.access)
		response = self.client.post(
			self.assignment_url,
			{
				"reviewers": [self.username, self.reviewer_username],
				"karil_id": 0xB0BACAFE
			}, format='json'
		)

		self.assertEquals(response.status_code, 404)