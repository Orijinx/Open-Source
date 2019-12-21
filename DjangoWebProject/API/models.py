from django.db import models
# Это файл для работы с таблица sqlite3

# Создание таблицы с полями


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    # метод для вывода в admin'ке имени всех авторов.

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(
        'Author', related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
