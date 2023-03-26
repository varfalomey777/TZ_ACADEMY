from django.test import TestCase
from .models import Book, Author, BookAndAuthor


class BookAndAuthorTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name="Иван",
            surname="Иванов",
            patronymic="Иванович",
            birthday="20.00.0101")
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

    def test_book(self):
        self.assertEqual(self.book.title, "Книга")
        self.assertEqual(self.book.photo, "photo.jpg")
        self.assertEqual(self.book.year, "2022")
        self.assertEqual(self.book.genre, "Фантастика")
        self.assertEqual(self.book.pages, "300")

    def test_author(self):
        self.assertEqual(self.author.name, "Иван")
        self.assertEqual(self.author.surname, "Иванов")
        self.assertEqual(self.author.patronymic, "Иванович")
        self.assertEqual(self.author.birthday, "20.00.0101")
