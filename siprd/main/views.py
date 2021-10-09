from .serializers import UserSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from .models import User
import logging

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

logger = logging.getLogger(__name__)

# Register API
# Will create a new user in database if valid
class Register(APIView):
	def post(self, request):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			account = serializer.save()
			if account:
				return Response(status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Fetches the data of the user who is currently logged in
class ViewUserData(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request):
		username = request.user.username
		user = User.objects.filter(username=username).first()
		serializer = UserSerializer(user)

		return Response(serializer.data)

# Will return all user data for the given email
# only succeeds if the authenticated user's email
# is the one being queried
# For use with Google auth, to check for similar emails
class GetLinkedUsers(APIView):
	def get(self, request):
		logger.info("Checking for linked users...")
		requested_email = request.query_params['email']

		matches = User.objects.filter(email=requested_email)
		usernames = []
		for user in matches:
			usernames.append(user.username)
		logger.info(f"{len(usernames)} Matches found!")

		if len(usernames) != 0:
			response = {}
			response['usernames'] =  usernames
			return Response(response, status=status.HTTP_200_OK)
		else:
			# No matching usernames
			return Response(status=status.HTTP_204_NO_CONTENT)

# Get user data
# For use with getting user roles for authorization and others.
def get_user_data(request):
	username = request.user.username
	user = User.objects.filter(username=username).first()
	serializer = UserSerializer(user)
	return serializer.data

# User Management API
# Handles Admin/SDMPT management of user accounts
class ManageUsers(APIView):
	permission_classes = [IsAuthenticated]
	forbidden_role_msg = {'message': 'You must be an Admin or SDM PT to perform this action.'}

	# Fetches all user data
	def get(self, request):
		user_data = get_user_data(request)
		user_role = user_data['role']
		
		if ( user_role == "Admin" or user_role == "SDM PT" ):
			user_list = User.objects.all().order_by("date_joined")

			serializer = UserSerializer(user_list, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
		else: return Response(self.forbidden_role_msg, status=status.HTTP_401_UNAUTHORIZED)


	# Create new dosen
	# Same as registration..
	# but done by an authenticated admin or SDMPT.
	def post(self, request):
		user_data = get_user_data(request)
		user_role = user_data['role']
		
		if ( user_role == "Admin" or user_role == "SDM PT" ):
			register_view = Register()
			return Register.post(register_view, request)
		else: return Response(self.forbidden_role_msg, status=status.HTTP_401_UNAUTHORIZED)

	# Gets the user data with a certain username --> Edits according to the request
	# Username in request body
	# Accessible for Admins, SDM PT, and users who want to edit their own account.
	def put(self, request):
		user_data = get_user_data(request)
		user_role = user_data['role']

		if ( user_role == "Admin" or user_role == "SDM PT" or user_data['username'] == request.data['username']):
			try:
				user = User.objects.get(username=request.data['username'])
			except User.DoesNotExist:
				return Response({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
			user = User.objects.get(username=request.data['username'])

			serializer = UserSerializer(user, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else: return Response(self.forbidden_role_msg, status=status.HTTP_401_UNAUTHORIZED)

	# Fetches data with a certain username, then deletes it.
	# Username in request body
	def delete(self, request):
		user_data = get_user_data(request)
		user_role = user_data['role']

		if ( user_role == "Admin" or user_role == "SDM PT" ):
			try:
				user = User.objects.get(username=request.data['username'])
			except User.DoesNotExist: 
				return Response({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
			user.delete()
			return Response({request.data['username'] + ' was deleted successfully!'}, status=status.HTTP_200_OK)
		else: return Response(self.forbidden_role_msg, status=status.HTTP_401_UNAUTHORIZED)

# Test view for user authentication
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ping_auth(request):
	return JsonResponse({'message': 'You are logged in!'})

# General ping test
def ping(request):
	if request.method == "GET":
		return JsonResponse({'foo': 'bar'})