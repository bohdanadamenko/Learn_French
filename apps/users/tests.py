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


class RegistrationValidationTest(TestCase):
    """Tests for username and password validation rules during registration."""

    def test_valid_registration(self):
        """Test valid registration with min 4 chars, letters, digits, and !_-."""
        from apps.users.views import SignUpForm
        form = SignUpForm(data={
            "username": "u_1-!",
            "email": "valid@example.com",
            "password1": "p_4-!",
            "password2": "p_4-!",
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_username_too_short(self):
        """Test username with less than 4 characters is rejected."""
        from apps.users.views import SignUpForm
        form = SignUpForm(data={
            "username": "abc",
            "email": "short@example.com",
            "password1": "valid123",
            "password2": "valid123",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)

    def test_username_invalid_characters(self):
        """Test username with invalid characters (e.g. @, space) is rejected."""
        from apps.users.views import SignUpForm
        form = SignUpForm(data={
            "username": "user@name",
            "email": "invalid_char@example.com",
            "password1": "valid123",
            "password2": "valid123",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)

    def test_password_too_short(self):
        """Test password with less than 4 characters is rejected."""
        from apps.users.views import SignUpForm
        form = SignUpForm(data={
            "username": "valid_user",
            "email": "short_pass@example.com",
            "password1": "123",
            "password2": "123",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)

    def test_password_invalid_characters(self):
        """Test password with invalid characters (e.g. #, space) is rejected."""
        from apps.users.views import SignUpForm
        form = SignUpForm(data={
            "username": "valid_user",
            "email": "invalid_pass@example.com",
            "password1": "pass#12",
            "password2": "pass#12",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)
