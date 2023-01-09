from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from posts.permissions import SafeMethodOrIsPostAuthorOrAdmin
from posts.serializers import PostSerializer, PostCreateSerializer

User = get_user_model()

class ListCreatePostView(ListCreateAPIView):
    """
    get:
    Lists all posts of all users in chronological order.

    post:
    Creates a new Post with logged-in user as author.
    """
    queryset = Post.objects.all().order_by('-created')
    serializer_class = PostSerializer
    permission_classes = [SafeMethodOrIsPostAuthorOrAdmin]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class RetrieveUpdateDeletePostView(RetrieveUpdateDestroyAPIView):
    """
        get:
        Retrieves a specific Post by ID and displays all the information about that Post.

        put:
        Updates a specific Post (only allowed to Post author or admin).

        patch:
        Updates a specific Post (only allowed to Post owner or admin). It allows partial update.

        delete:
        Deletes a Post by ID (only allowed to Post owner or admin).

    """
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [SafeMethodOrIsPostAuthorOrAdmin]


class ToggleLikeView(GenericAPIView):
    """
    post:
    toggle like/unlike a specific Post.
    """
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs.get('pk'))
        if post.liked_by.filter(email=request.user.email).exists():
            post.liked_by.remove(request.user.id)
        else:
            post.liked_by.add(request.user)

        return HttpResponse(status=204)


class ListLikedPostView(ListAPIView):
    """
    get:
    Lists posts the logged-in user likes in chronological order.
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Post.objects.filter(liked_by=user_id).order_by('-created')

        return queryset

class ListFollowingPostView(ListAPIView):
    """
    get:
    Lists all posts from users that the logged-in user is following in chronological order.
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        following = [user.id for user in self.request.user.following.all()]
        queryset = [post for post in Post.objects.all().order_by('-created') if post.author_id in following]

        return queryset


class ListUserPostView(ListAPIView):
    """
    get:
    Lists all posts from a given user in chronological order.
    """
    serializer_class = PostSerializer

    def get_queryset(self):
        given_user_id = self.kwargs.get("pk")
        queryset = Post.objects.filter(author_id=given_user_id).order_by('-created')

        return queryset


