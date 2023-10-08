from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    category = models.ForeignKey('Menu', on_delete=models.CASCADE)
    about = models.TextField(verbose_name='Содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Menu(models.Model):
    title = models.CharField(
        'Заголовок', max_length=100, unique=True)
    about = models.TextField(
        'Описание', max_length=350, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

class MenuItem(models.Model):
    title = models.CharField(
        'Заголовок', max_length=100, unique=True)
    about = models.TextField(
        'Описание', max_length=350, blank=True)
    url = models.URLField(
        verbose_name='URL ссылка', max_length=100, blank=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='menu_items')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

