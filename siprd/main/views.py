from .serializers import UserSerializer
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt, datetime

def homepage(request):
	return render(request=request, template_name='main/home.html')

# Register API
class RegisterAPI(APIView):
	def post(self, request):
		serializer = UserSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)

class LoginAPI(APIView):
	def post(self, request):
		username = request.data['username']
		password = request.data['password']

		user = User.objects.filter(username=username).first()

		if user is None:
			raise AuthenticationFailed('User not found!')

		if not user.check_password(password):
			raise AuthenticationFailed('Incorrect Password!')

		payload = {
			'username': user.username, 
			'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60), # expiration date
			'iat': datetime.datetime.utcnow()									# creation date
		}

		# FIXME: Hide secret key as env variable in production
		token = jwt.encode(payload, 'secret', algorithm='HS256')
		# decoded = jwt.decode(token, 'secret', algorithms=['HS256'])

		response = Response()
		
		response.set_cookie(key='jwt', value=token, httponly=True)
		response.data = {
			'jwt': token,
		}

		return response 

class UserAPI(APIView):
	def get(self, request):
		token = request.COOKIES.get('jwt')

		if not token:
			raise AuthenticationFailed('You are not authenticated.')
		
		try:
			payload = jwt.decode(token, 'secret', algorithms=['HS256'])
		except jwt.ExpiredSignatureError:
			raise AuthenticationFailed('You are not authenticated.')

		user = User.objects.filter(username=payload['username']).first()
		serializer = UserSerializer(user)

		return Response(serializer.data)

class LogoutAPI(APIView):
	def post(self, request):
		response = Response()
		response.delete_cookie('jwt')
		response.data = {
			'message': 'Log out success.'
		}

		return response

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def ping(request):
	if request.method == "GET":
		return JsonResponse({'foo': 'bar'})