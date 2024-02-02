from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from .views import index, profile
from .models import Profile
from django.contrib.auth.models import User


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse("profiles:index")
        self.assertEqual(resolve(url).func, index)

    def test_profile_url_is_resolved(self):
        """Testează dacă URL-ul pentru profilul utilizatorului este rezolvat corect."""
        url = reverse("profiles:profile", args=["testuser"])
        self.assertEqual(resolve(url).func, profile)


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.profile = Profile.objects.create(user=self.user)

    def test_index_view(self):
        """Testează dacă view-ul index este accesibil și returnează statusul corect."""
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")
        self.assertTrue("profiles_list" in response.context)

    def test_profile_view(self):
        """Testează dacă view-ul profile este accesibil pentru un username valid."""
        response = self.client.get(
            reverse("profiles:profile", kwargs={"username": "testuser"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertTrue("profile" in response.context)

        # Verifică dacă profilul din context este cel corect
        profile_in_context = response.context["profile"]
        self.assertEqual(profile_in_context.user.username, "testuser")
