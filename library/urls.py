from django.urls import path
from .views import library_list


urlpatterns = [
    path('library/', library_list),
]