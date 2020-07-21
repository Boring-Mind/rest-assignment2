from django.contrib.auth.models import User
from rest_framework import serializers
from drf_nested_fields.serializers import NestedFieldsSerializerMixin

from user.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = UserProfile.objects.create(**profile_data, **validated_data)
        return user


class ProfileSerializer(NestedFieldsSerializerMixin, serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'photo']
        nested_fields = {
            'user': (
                ['id'],
                ['username'],
                ['email'],
            )
        }

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        profile = UserProfile.objects.create(
            username=user_data.username,
            email=user_data.email,
            password=user_data.password,
            **validated_data
        )
        return profile
