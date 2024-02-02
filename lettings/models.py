from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    A model for storing address details.

    Attributes:
        number: Street number.
        street: Street name.
        city: City name.
        state: State abbreviation.
        zip_code: Postal zip code.
        country_iso_code: ISO country code.

    Returns a string representation combining number and street.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    A model representing a letting, linked to an address.

    Attributes:
        title: Title of the letting.
        address: Associated Address instance.

    Returns the title as its string representation.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
