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

# Gets the user data with a certain username --> Edits according to the request
# Takes URL /api/edit/<username>
class EditUserData(APIView):
	# permission_classes = [IsAuthenticated]

	def put(self, request, uname):
		try:
			user = User.objects.get(username=uname)
		except User.DoesNotExist: 
        		return Response({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
		user = User.objects.get(username=uname)

		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# Fetches data with a certain username, then deletes it.
# Takes URL /api/delete/<username>
class DeleteDosen(APIView):
	# permission_classes = [IsAuthenticated]

	def delete(self, request, uname):
		# if request.method == 'DELETE' & request.user.role == 'Admin':
		try:
			user = User.objects.get(username=uname)
		except User.DoesNotExist: 
        		return Response({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
		user.delete()
		return Response({uname + ' was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# Will return usernames linked to the given email
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

# Test view for user authentication
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ping_auth(request):
	return JsonResponse({'message': 'You are logged in!'})

# General ping test
def ping(request):
	if request.method == "GET":
		return JsonResponse({'foo': 'bar'})