import os
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import views
from .views.index_view import IndexView
from .views.api.scenarios_api import ScenariosAPI

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
API URLs
"""
urlpatterns += [
    re_path(r'^api/scenarios', ScenariosAPI.as_view(), name="scenario"),
]

"""
Debug URLs
"""
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve, {'document_root': os.path.join(settings.BASE_DIR, 'trustlab\static')}),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

