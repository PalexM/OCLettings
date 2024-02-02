from django.shortcuts import render
from django.http import HttpResponseServerError
from .models import Letting
import sentry_sdk


def index(request):
    """
    Renders a list of all lettings.

    Fetches all letting instances from the database and passes them to
    the 'lettings/index.html' template for rendering.

    Parameters:
        request: The HTTP request object.

    Returns:
        HttpResponse: An HttpResponse object that renders the lettings list template.
    """

    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Renders details for a specific letting.

    Fetches a letting instance by its ID and passes its details to
    the 'lettings/letting.html' template for rendering.

    Parameters:
        request: The HTTP request object.
        letting_id: The ID of the letting to display.

    Returns:
        HttpResponse: An HttpResponse object that renders the letting detail template.
    """

    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
