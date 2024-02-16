from django.urls import path
from .views import *

urlpatterns = [
    path('', mainmenu),
    path('contents', contents, name='contents'),
]
