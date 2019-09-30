from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.index_view import IndexView

urlpatterns = [
    path(r'', IndexView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

