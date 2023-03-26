from django.core.validators import RegexValidator
from django.db import models


class Book(models.Model):
    title: models.CharField = models.CharField(
        max_length=30, verbose_name="Название книги"
    )
    genre: models.CharField = models.CharField(
        max_length=30, verbose_name="Жанр")
    author: models.ManyToManyField = models.ManyToManyField(
        "Author",
        verbose_name="Автор",
        through="BookAndAuthor",
        through_fields=("book", "author", "fio"),
    )
    year: models.IntegerField = models.IntegerField(verbose_name="Год издания")
    pages: models.IntegerField = models.IntegerField(
        verbose_name="Количество страниц")
    photo: models.ImageField = models.ImageField(
        verbose_name="Фотография книги", upload_to="all_photos/%Y/%m/%d/"
    )

    def save(self, *args, **kwargs) -> None:
        self.title, self.genre = self.title.capitalize(), self.genre.capitalize()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.title},{self.genre},{self.author},{self.year},{self.pages},{self.photo}"


class Author(models.Model):
    surname: models.CharField = models.CharField(
        max_length=30, verbose_name="Фамилия")
    name: models.CharField = models.CharField(
        max_length=30, verbose_name="Имя")
    patronymic: models.CharField = models.CharField(
        max_length=30, verbose_name="Отчество"
    )
    birthday = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                r"^\d{2}\.\d{2}\.\d{4}$",
                "Дата должна быть в формате dd.mm.yyyy")],
        verbose_name="День рождения",
    )
    fio: models.CharField = models.CharField(max_length=30)

    def save(self, *args, **kwargs) -> None:
        self.surname, self.name, self.patronymic = (
            self.surname.capitalize(),
            self.name.capitalize(),
            self.patronymic.capitalize(),
        )
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.fio}"


class BookAndAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    fio = models.CharField(max_length=30)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.author:
            self.fio = f"{self.author.fio}"

    def __str__(self) -> str:
        return f"{self.book},{self.author},{self.fio}"
