import os

from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import smart_bytes, smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.generics import UpdateAPIView
from .util import Util
from .serializers import UserSerializer, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer
from django.http import JsonResponse, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from .models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator

import logging

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

logger = logging.getLogger(__name__)


class CustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


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


# Fetches the data of the user who is currently logged in
class IsUserExist(APIView):

    def post(self, request):
        req_data = request.data

        username = req_data.get('username')
        user = User.objects.filter(username=username).first()
        print(user.email)
        if user is None:
            return Response(status=404, data="username not found")

        return Response(status=201, data="bruh")


# Will return all user data for the given email
# only succeeds if the authenticated user's email
# is the one being queried
# For use with Google auth, to check for similar emails
class CheckLinkedUsers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logger.info("Checking for linked users...")
        username = request.user.username
        user = User.objects.filter(username=username).first()
        user = UserSerializer(user)
        logger.info("User found!")

        user_email = user.data.get('email')
        logger.info("User email: " + user_email)
        requested_email = UserSerializer(data=request.data).data.get('email')
        logger.info("Requested email: " + requested_email)
        if user_email == requested_email:
            matches = User.objects.filter(email=user_email).all()
            serializer = UserSerializer(matches, many=True)
            logger.info("Matches found!")
            return Response(serializer.data)
        else:
            return Response("You are not authorized!", status=status.HTTP_401_UNAUTHORIZED)


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
                relativeLink = reverse('main:password-reset-confirm',
                                       kwargs={'uidb64': uidb64, 'token': token, 'username': username})

                redirect_url = request.data.get('redirect_url', '')
                absurl = 'http://' + current_site + relativeLink
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

            except UnboundLocalError as e:
                # TODO change for production
                return HttpResponseRedirect("http://localhost:8080/token-error")


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)


# Test view for user authentication
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ping_auth(request):
    return JsonResponse({'message': 'You are logged in!'})


# General ping test
def ping(request):
    if request.method == "GET":
        return JsonResponse({'foo': 'bar'})
