from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(required=False)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'full_name',
            'university',
            'nip',
            'field_of_study',
            'position',
            'role',
            'approved',
            'date_joined'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def get_validation_exclusions(self):
        exclusions = super(UserSerializer, self).get_validation_exclusions()
        return exclusions + ['date_joined']

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=25)

    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['username', 'redirect_url']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return user
        except Exception:
            raise AuthenticationFailed('The reset link is invalid', 401)
