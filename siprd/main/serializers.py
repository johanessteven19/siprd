from rest_framework import serializers
from .models import User

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