from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Group, Post
from api.permission import OwnerOrReadOnly
from api.serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с постами.
    Позволяет выполнять CRUD-операции, проверяя авторство поста.
    При создании поста автор автоматически назначается текущим пользователем.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """
        Переопределяет метод сохранения поста, чтобы автор
        был автоматически установлен как текущий пользователь.
        """
        serializer.save(author=self.request.user)


class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    ViewSet для подписок на других пользователей.
    Позволяет создавать и просматривать подписки текущего пользователя.
    """
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """
        Возвращает список пользователей, на которых
        подписан текущий пользователь.
        """
        return self.request.user.followers.all()

    def perform_create(self, serializer):
        """
        Переопределяет метод создания, чтобы пользователь
        был автоматически установлен как текущий пользователь.
        """
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для работы с группами. Доступен только для чтения.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny,)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с комментариями к постам.
    Позволяет выполнять CRUD-операции с комментариями.
    Проверяет авторство комментария перед изменением или удалением.
    """
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly,)

    def get_queryset(self):
        """
        Возвращает все комментарии к конкретному посту.
        Пост определяется по 'post_id', переданному в URL.
        """
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        """
        Переопределяет метод создания, чтобы комментарий
        был привязан к посту и автором был установлен текущий пользователь.
        """
        post = self.get_post()
        serializer.save(post=post, author=self.request.user)

    def get_post(self):
        """
        Возвращает пост, соответствующий 'post_id' из URL.
        """
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))
