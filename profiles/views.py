from django.shortcuts import render
from .models import Profile
from django.http import HttpResponseServerError
import sentry_sdk


def index(request):
    """
    Renders a list of all user profiles.

    Fetches all profile instances from the database and passes them to
    the 'profiles/index.html' template for display.

    Parameters:
        request: The HTTP request object.

    Returns:
        HttpResponse: An HttpResponse object that renders the list of profiles.
    """

    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Renders the details of a specific user profile.

    Fetches a profile instance by the username of the associated user and passes it to
    the 'profiles/profile.html' template for display.

    Parameters:
        request: The HTTP request object.
        username: The username of the user whose profile is to be displayed.

    Returns:
        HttpResponse: An HttpResponse object that renders the detailed view of a user's profile.
    """

    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
