from rest_framework import serializers

from registration_profiles.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'email',
                  'username',
                  'first_name',
                  "last_name",
                  "last_login",
                  "is_superuser",
                  "is_staff",
                  "is_active",
                  "date_joined",
                  "groups",
                  "following",
                  "followed_by"]