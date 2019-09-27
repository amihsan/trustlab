from django.urls import path
from . import views
# from .views.index_view import IndexView

urlpatterns = [
    path('', views.home, name="home"),
]