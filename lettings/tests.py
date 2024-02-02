from django.test import SimpleTestCase
from django.urls import reverse, resolve
from lettings.views import index, letting
from django.test import TestCase, Client
from lettings.models import Letting, Address


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse("lettings:index")
        self.assertEqual(resolve(url).func, index)

    def test_letting_url_is_resolved(self):
        # Presupunând că există un letting cu id=1 pentru test
        url = reverse("lettings:letting", args=[1])
        self.assertEqual(resolve(url).func, letting)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.address = Address.objects.create(
            street="Strada Exemplu",
            number=5,
            zip_code=34534,
            state="CA",
            country_iso_code=312,
            city="Baia Mare",
        )
        self.letting = Letting.objects.create(
            title="Apartament 1",
            address=self.address,
        )

    def test_lettings_index_view(self):
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_letting_view(self):
        response = self.client.get(reverse("lettings:letting", args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")
