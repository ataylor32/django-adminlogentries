from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse

from admin_log_entries.settings import compute_settings


class AdminViewsTest(TestCase):
    fixtures = [
        'test_data.json',
    ]

    def setUp(self):
        self.client.login(
            username='superuser',
            password='testing!',
        )

    def test_index(self):
        compute_settings()
        url = reverse('admin:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn(
            '<a href="/admin/admin/logentry/">Log entries</a>',
            content
        )

    @override_settings(
        ADMIN_LOG_ENTRIES={'has_module_permission_false': True},
    )
    def test_index_has_module_permission_false(self):
        compute_settings()
        url = reverse('admin:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertNotIn(
            '<a href="/admin/admin/logentry/">Log entries</a>',
            content
        )

    def test_changelist(self):
        compute_settings()
        url = reverse('admin:admin_logentry_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertIn('<a href="/admin/admin/">Administration</a>', content)

    @override_settings(
        ADMIN_LOG_ENTRIES={'has_module_permission_false': True},
    )
    def test_changelist_has_module_permission_false(self):
        compute_settings()
        url = reverse('admin:admin_logentry_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        content = response.content.decode('utf-8')
        self.assertNotIn('<a href="/admin/admin/">Administration</a>', content)

    def test_add(self):
        compute_settings()
        url = reverse('admin:admin_logentry_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_change(self):
        compute_settings()
        url = reverse('admin:admin_logentry_change', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_delete(self):
        compute_settings()
        url = reverse('admin:admin_logentry_delete', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_history(self):
        compute_settings()
        url = reverse('admin:admin_logentry_history', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
