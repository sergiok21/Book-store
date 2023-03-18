from django.test import TestCase

from books.models import Book, BookCategory


class BookTestCase(TestCase):

    def test_book_category(self):
        category_create = BookCategory.objects.create(name='Category')
        category_create.save()

        self.assertEqual(category_create, BookCategory.objects.first())

        category_create = BookCategory.objects.create(name='Category2')
        category_create.save()

        self.assertEqual(category_create, BookCategory.objects.last())

    def test_book(self):
        category_create = BookCategory.objects.create(name='Category')
        category_create.save()

        book_create = Book.objects.create(
            name='Name', description='Description', price=100, quantity=2, category=category_create
        )
        book_create.save()

        self.assertEqual(book_create, Book.objects.first())

        book_create = Book.objects.create(
            name='Name2', description='Description2', price=1000, quantity=3, category=category_create
        )
        book_create.save()

        self.assertEqual(book_create, Book.objects.last())

        Book.objects.last().delete()
        book_create = Book.objects.last()

        self.assertEqual(book_create, Book.objects.last())
        self.assertEqual(len(list(Book.objects.all())), 1)
