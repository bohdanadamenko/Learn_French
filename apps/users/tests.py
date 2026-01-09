"""
Tests for the users app.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTest(TestCase):
    """Tests for the custom User model."""

    def test_create_user(self):
        """Test creating a regular user. 👤"""
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("testpass123"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Test creating a superuser. 👑"""
        admin = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpass123"
        )
        self.assertEqual(admin.username, "admin")
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    def test_email_unique(self):
        """Test that email must be unique. 📧"""
        User.objects.create_user(
            username="user1",
            email="unique@example.com",
            password="pass123"
        )
        with self.assertRaises(Exception):
            User.objects.create_user(
                username="user2",
                email="unique@example.com",  # Duplicate email
                password="pass123"
            )

    def test_user_str(self):
        """Test the __str__ method returns username. 🆔"""
        user = User.objects.create_user(
            username="displayname",
            email="display@example.com",
            password="pass123"
        )
        self.assertEqual(str(user), "displayname")
