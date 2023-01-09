from django.urls import path

from posts.views import RetrieveUpdateDeletePostView, ListCreatePostView, ToggleLikeView, ListLikedPostView, \
    ListFollowingPostView, ListUserPostView

urlpatterns = [
    path('', ListCreatePostView.as_view()),
    path('<int:pk>/', RetrieveUpdateDeletePostView.as_view()),
    path('toggle-like/<int:pk>/', ToggleLikeView.as_view()),
    path('likes/', ListLikedPostView.as_view()),
    path('following/', ListFollowingPostView.as_view()),
    path('users/<int:pk>/', ListUserPostView.as_view()),
]