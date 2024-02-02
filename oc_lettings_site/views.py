from django.shortcuts import render


def index(request):
    """
    Renders the main homepage.

    Parameters:
        request: The HTTP request object.

    Returns:
        HttpResponse: Renders the 'index.html' template.
    """
    return render(request, "index.html")


def custom_404_error(request, exception):
    """
    Custom 404 error handler.

    Displays a custom 404 error page when a page is not found.

    Parameters:
        request: The HTTP request object.
        exception: The exception that triggered the 404 error.

    Returns:
        HttpResponse: Renders the '404.html' template with a 404 status code.
    """
    return render(request, "404.html", status=404)


def custom_500_error(request, exception):
    """
    Custom 500 error handler.

    Displays a custom 500 error page when a server error occurs.

    Parameters:
        request: The HTTP request object.
        exception: The exception that triggered the 500 error.

    Returns:
        HttpResponse: Renders the '500.html' template with a 500 status code.
    """
    return render(request, "500.html", status=500)
