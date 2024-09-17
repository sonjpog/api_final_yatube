from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с данными модели Post.
    """
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class FollowSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с данными модели Follow.
    """
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following',),
                message="Нельзя подписаться второй раз."
            ),
        )

    def validate(self, validated_data):
        """
        Валидация отдельного поля following.
        """
        user = self.context['request'].user
        following = validated_data['following']
        if user == following:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя.')
        return validated_data


class GroupSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с данными модели Group.
    """
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с данными модели Comment.
    """
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
