from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Configures the 'lettings' app within a Django project.

    This class sets up the application name and is necessary for Django to recognize
    the 'lettings' app. It should be included in the INSTALLED_APPS setting of the
    project's settings.py to be active.

    Attributes:
        name (str): The name of the application, 'lettings'.
    """

    name = "lettings"
