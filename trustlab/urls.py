from django.urls import path
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]