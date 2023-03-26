from django.test import TestCase, Client
from django.urls import reverse
from .models import Book, Author, BookAndAuthor


class BookAndAuthorTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name="Иван",
            surname="Иванов",
            patronymic="Иванович",
            birthday="20.00.0101"
        )
        self.book = Book.objects.create(
            title="Книга",
            photo="photo.jpg",
            year="2022",
            genre="Фантастика",
            pages="300",
        )

    def test_book_author_creation(self):
        self.book.author.set([self.author])
        book_author = BookAndAuthor.objects.first()
        self.assertEqual(book_author.book, self.book)
        self.assertEqual(book_author.author, self.author)
        self.assertEqual(book_author.author, self.author)
