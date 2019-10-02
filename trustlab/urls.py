import os
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import views
from django.urls import re_path
from .views.index_view import IndexView

urlpatterns = [
    path(r'', IndexView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve, {'document_root': os.path.join(settings.BASE_DIR, 'trustlab\static')}),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

