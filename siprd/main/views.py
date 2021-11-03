<<<<<<< Updated upstream
from .serializers import UserSerializer
from django.http import JsonResponse
from rest_framework import status
=======
import os

from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import smart_bytes, smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.generics import UpdateAPIView
from .util import Util
from .serializers import KaryaIlmiahSerializer, ReviewSerializer, UserSerializer, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer
from django.http import JsonResponse, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from rest_framework import status, generics
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
	permission_classes = [IsAuthenticated]
	forbidden_role_msg = {'message': 'You must be an Admin or SDM PT to perform this action.'}

	# Fetches all user data
	def get(self, request):
		user_data = get_user_data(request)
		user_role = user_data['role']
		
		if ( user_role == "Admin" or user_role == "SDM PT" ):
			user_list = User.objects.all().order_by("date_joined").reverse()

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
=======
    permission_classes = [IsAuthenticated]
    forbidden_role_msg = {'message': 'You must be an Admin or SDM PT to perform this action.'}

    # Fetches all user data
    def get(self, request):
        user_data = get_user_data(request)
        user_role = user_data['role']
        
        if ( user_role == "Admin" or user_role == "SDM PT" ):
            user_list = User.objects.all().order_by("date_joined").reverse()

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

            serializer = UserSerializer(user, data=request.data, partial=True)
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

class ReviewForm(APIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = KaryaIlmiahSerializer

    def post(self, request):
        if request.method == 'POST':
            serializer = KaryaIlmiahSerializer(data = request.data)
            if serializer.is_valid():
                review = serializer.save()
                if review:
                    return Response(status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = ResetPasswordEmailRequestSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                if user is None:
                    return Response({'failed': "user not found"}, status=404)
                uidb64 = urlsafe_base64_encode(smart_bytes(user.pk))
                token = PasswordResetTokenGenerator().make_token(user)
                current_site = get_current_site(
                    request=request).domain
                relative_link = reverse('main:password-reset-confirm',
                                       kwargs={'uidb64': uidb64, 'token': token, 'username': username})

                redirect_url = request.data.get('redirect_url', '')
                absurl = 'http://' + current_site + relative_link
                email_body = 'Hello, \n Use link below to reset your password  \n' + \
                             absurl + "?redirect_url=" + redirect_url
                data = {'email_body': email_body, 'to_email': user.email,
                        'email_subject': 'Reset your passsword'}
                # Util.send_email(data)
                return Response({'success': 'We have sent you a link to reset your password', 'data': absurl},
                                status=status.HTTP_200_OK)
            else:
                return Response({'failed': "user not found"}, status=404)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token, username):

        redirect_url = request.GET.get('redirect_url')

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, please request a new one'},
                                status=status.HTTP_400_BAD_REQUEST)
            # TODO change for production
            print(uidb64)
            return HttpResponseRedirect("http://localhost:8080/reset-password/" + token + "/" + username + "/" + uidb64)

        except DjangoUnicodeDecodeError as identifier:
            try:
                if not PasswordResetTokenGenerator().check_token(user):
                    # TODO change for production
                    return HttpResponseRedirect("http://localhost:8080/token-error")

            except UnboundLocalError:
                # TODO change for production
                return HttpResponseRedirect("http://localhost:8080/token-error")


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)

>>>>>>> Stashed changes

# Test view for user authentication
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ping_auth(request):
	return JsonResponse({'message': 'You are logged in!'})

# General ping test
def ping(request):
	if request.method == "GET":
		return JsonResponse({'foo': 'bar'})