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

# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter

# User Management API
# Handles Admin/SDMPT management of user accounts
class ManageUsers(APIView):
	permission_classes = [IsAuthenticated]

	# Create new dosen
	# Same as registration..
	# but done by an authenticated admin or SDMPT.
	def post(self, request):
		register_view = Register()
		return Register.post(register_view, request)

# Test view for user authentication
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def pingAuth(request):
	return JsonResponse({'message': 'You are logged in!'})

# General ping test
def ping(request):
	if request.method == "GET":
		return JsonResponse({'foo': 'bar'})