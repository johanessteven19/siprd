from .serializers import UserSerializer
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from rest_social_auth.views import SocialJWTPairOnlyAuthView
from .models import User

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from rest_auth.registration.views import SocialLoginView

def homepage(request):
	return render(request=request, template_name='main/home.html')

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
class CheckLinkedUsers(APIView):
	permission_classes = [IsAuthenticated]
	
	def get(self, request):
		user_email = request.user.email
		requested_email = UserSerializer(data=request.data).data.get('email')
		if user_email == requested_email:
			matches = User.objects.filter(email=user_email).all()
			serializer = UserSerializer(matches, many=True)
			return Response(serializer.data)
		else: return Response("You are not authorized!", status=status.HTTP_401_UNAUTHORIZED)



# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter

# Test view for user authentication
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def pingAuth(request):
	return JsonResponse({'message': 'You are logged in!'})

# General ping test
def ping(request):
	if request.method == "GET":
		return JsonResponse({'foo': 'bar'})