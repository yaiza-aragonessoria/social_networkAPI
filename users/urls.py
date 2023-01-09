from django.urls import path
from rest_framework.generics import ListAPIView

from registration_profiles.models import User
from users.serializers import UserSerializer
from users.views import ToggleFollow, ListFollowersView, ListFollowingView

urlpatterns = [
    path('', ListAPIView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer)),
    path('toggle-follow/<int:pk>/', ToggleFollow.as_view()),
    path('followers/', ListFollowersView.as_view()),
    path('following/', ListFollowingView.as_view()),
]
