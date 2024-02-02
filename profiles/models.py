from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    User profile model extending the default Django User model.

    Attributes:
        user (OneToOneField): A one-to-one link to Django's User model, ensuring each user has one unique profile.
        favorite_city (CharField): The user's favorite city, optional.

    Methods:
        __str__(self): Returns the username of the associated user, facilitating identification in the admin interface.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
