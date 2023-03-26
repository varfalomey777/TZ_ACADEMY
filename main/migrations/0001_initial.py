# Generated by Django 4.1.7 on 2023-03-26 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("surname", models.CharField(max_length=30, verbose_name="Фамилия")),
                ("name", models.CharField(max_length=30, verbose_name="Имя")),
                (
                    "patronymic",
                    models.CharField(max_length=30, verbose_name="Отчество"),
                ),
                (
                    "birthday",
                    models.DecimalField(
                        decimal_places=4, max_digits=10, verbose_name="День рождения"
                    ),
                ),
                ("fio", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=30, verbose_name="Название книги"),
                ),
                ("genre", models.CharField(max_length=30, verbose_name="Жанр")),
                ("year", models.IntegerField(verbose_name="Год издания")),
                ("pages", models.IntegerField(verbose_name="Количество страниц")),
                (
                    "photo",
                    models.ImageField(
                        upload_to="all_photos/%Y/%m/%d/",
                        verbose_name="Фотография книги",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookAndAuthor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fio", models.CharField(max_length=30)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.author"
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.book"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="author",
            field=models.ManyToManyField(
                through="main.BookAndAuthor", to="main.author", verbose_name="Автор"
            ),
        ),
    ]
