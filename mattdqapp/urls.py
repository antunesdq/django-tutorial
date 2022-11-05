from mattdqapp import views
from django.conf import settings
from django.urls import re_path

urlpatterns = [
    re_path(r'', views.simpleview)
]