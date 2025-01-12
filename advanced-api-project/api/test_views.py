from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User


class BookAPITestCase(TestCase):
    def setUp(self):
        self.valid_data = {
            "title": "Test Book",
            "author": "Test Author",
            "publication_year": 2024,
            # add other required fields here
        }
        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books with the correct author instances
        self.book1 = Book.objects.create(
            title="Book One",
            author=self.author1,
            publication_year=2001,
        )
        self.book2 = Book.objects.create(
            title="Book Two",
            author=self.author2,
            publication_year=2002,
        )

    # Test List View
    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Test Detail View
    def test_retrieve_book(self):
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # Test Create View
    def test_create_book(self):
        response = self.client.post('/api/books/create/', data=self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.valid_data['title'])

    # Test Update View
    def test_update_book(self):
        response = self.client.put(f'/api/books/{self.book1.id}/update/', data=self.update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, self.update_data['title'])

    # Test Delete View
    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book1.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # Test Filtering
    def test_filter_books_by_author(self):
        response = self.client.get('/api/books/?author=Author One')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], "Author One")

    # Test Searching
    def test_search_books(self):
        response = self.client.get('/api/books/?search=Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    # Test Ordering
    def test_order_books_by_publication_year(self):
        response = self.client.get('/api/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2001)

    # Test Permissions
    def test_unauthorized_access_to_create(self):
        self.client.logout()
        response = self.client.post('/api/books/create/', data=self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class MyViewTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_some_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='password')
        
        # Now you can test authenticated views
        response = self.client.get('/api/some_view/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
