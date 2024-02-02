from django.contrib import admin
from django.urls import path, include
from .views import index


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", index, name="index"),
    path("lettings/", include(("lettings.urls", "lettings"), namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
]
