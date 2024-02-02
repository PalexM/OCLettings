from django.test import TestCase
from django.urls import reverse


class TestError(TestCase):
    def test_admin_url_is_resolved(self):
        url = reverse("admin:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith("/admin/login/"))

    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_custom_404_view(self):
        response = self.client.get("/nonexistent_page/")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
