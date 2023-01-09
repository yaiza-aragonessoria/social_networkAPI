from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from users.serializers import UserSerializer

User = get_user_model()


class ToggleFollow(GenericAPIView):
    """
    post:
    toggle follow/unfollow a specific User.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        receiver = User.objects.get(id=kwargs.get('pk'))
        requester = User.objects.get(id=request.user.id)
        if receiver.followed_by.filter(email=request.user.email).exists():
            receiver.followed_by.remove(request.user.id)
            requester.following.remove(receiver.id)
        else:
            receiver.followed_by.add(request.user)
            requester.following.add(receiver)

        return HttpResponse(status=204)


class ListFollowersView(ListAPIView):
    """
    get:
    Lists all followers of the logged-in user.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.followed_by


class ListFollowingView(ListAPIView):
    """
    get:
    Lists all users that the logged-in user follows.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.following

