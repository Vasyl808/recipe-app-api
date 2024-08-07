"""
Tests for the Django admin modifications.
"""
from typing import Any
from django.http import HttpResponse

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Tests for Django admin."""

    def setUp(self) -> None:
        """Create user and client."""
        self.client: Client = Client()
        self.admin_user: Any = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        self.client.force_login(self.admin_user)
        self.user: Any = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User'
        )

    def test_users_lists(self) -> None:
        """Test that users are listed on page."""
        url: str = reverse('admin:core_user_changelist')
        res: HttpResponse = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self) -> None:
        """Test the edit user page works."""
        url: str = reverse('admin:core_user_change', args=[self.user.id])
        res: HttpResponse = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self) -> None:
        """Test the create user page works."""
        url: str = reverse('admin:core_user_add')
        res: HttpResponse = self.client.get(url)

        self.assertEqual(res.status_code, 200)
