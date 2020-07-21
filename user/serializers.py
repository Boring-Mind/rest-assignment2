from django.contrib.auth.models import User
from rest_framework import serializers

from user.models import UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    queryset = User.objects.all()
    user = serializers.PrimaryKeyRelatedField(queryset=queryset)
    photo = serializers.ImageField(allow_empty_file=True, use_url=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'photo']


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=254, min_length=6)
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = UserProfile.objects.create(**profile_data, **validated_data)
        return user
