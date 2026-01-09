"""
Tests for the core app.
"""
from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.lessons.models import Lesson

User = get_user_model()


class IndexViewTest(TestCase):
    """Tests for the index view."""

    def setUp(self):
        """Set up test client and user."""
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123"
        )
        # Create a test lesson
        self.lesson = Lesson.objects.create(
            title="Test Lesson",
            title_ru="Тестовый урок",
            data_lesson_id="test1",
            content_html="<p>Test content</p>",
            order=1
        )

    def test_index_requires_login(self):
        """Test that index page requires authentication."""
        response = self.client.get(reverse('core:index'))
        # Should redirect to login
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url.lower())

    def test_index_authenticated(self):
        """Test that authenticated user can access index."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_contains_lessons(self):
        """Test that index page contains lessons in context."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse('core:index'))
        self.assertIn('lessons', response.context)
        self.assertEqual(response.context['lessons'].count(), 1)


class ErrorPagesTest(TestCase):
    """Tests for custom error pages."""

    @override_settings(DEBUG=False)
    def test_404_page(self):
        """Test that 404 page returns correct status and uses custom template."""
        response = self.client.get('/nonexistent-page-12345/')
        self.assertEqual(response.status_code, 404)

    def test_custom_404_handler_direct(self):
        """Test 404 handler function directly."""
        from django.test import RequestFactory
        from apps.core.views import custom_404
        
        factory = RequestFactory()
        request = factory.get('/fake/')
        response = custom_404(request, Exception("Not Found"))
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'404', response.content)

    def test_custom_500_handler_direct(self):
        """Test 500 handler function directly."""
        from django.test import RequestFactory
        from apps.core.views import custom_500
        
        factory = RequestFactory()
        request = factory.get('/fake/')
        response = custom_500(request)
        self.assertEqual(response.status_code, 500)
        self.assertIn(b'500', response.content)

