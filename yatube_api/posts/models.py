from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Follow(models.Model):
    """
    Модель для подписок пользователей.
    Поле `user` — это подписчик.
    Поле `following` — это пользователь, на которого подписываются.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers',
        help_text='Пользователь, который подписывается'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followings',
        help_text='Пользователь, на которого подписываются'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'following',),
                name='unique_user_following'
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user} подписан на {self.following}'


class Group(models.Model):
    """
    Модель для групп публикаций.
    Группы могут содержать посты, объединённые общей темой.
    """
    title = models.CharField(max_length=100, help_text='Название группы')
    slug = models.SlugField(unique=True, max_length=50,
                            help_text='Уникальный слаг для группы')
    description = models.TextField(help_text='Описание группы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Post(models.Model):
    text = models.TextField(help_text='Текст публикации')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts',
        help_text='Автор публикации'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True,
        help_text='Изображение к публикации'
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, related_name='posts',
        blank=True, null=True,
        help_text='Группа, к которой относится публикация'
    )

    def __str__(self):
        return self.text[:30]

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date']


class Comment(models.Model):
    """
    Модель для комментариев к публикациям.
    Комментарии принадлежат определённым постам и пользователям.
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments',
        help_text='Автор комментария'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments',
        help_text='Пост, к которому относится комментарий'
    )
    text = models.TextField(help_text='Текст комментария')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True,
        help_text='Дата создания комментария'
    )

    def __str__(self):
        return f'Комментарий от {self.author} к посту {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created']
