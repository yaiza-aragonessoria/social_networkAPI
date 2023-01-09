from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()

    def get_like_count(self, instance):
        return 10

    class Meta:
        model = Post
        fields = ['id', 'content', 'author', 'like_count', 'created', 'liked_by']
        read_only_fields = ['author', 'like_count']


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author']