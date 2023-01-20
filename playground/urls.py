from django.urls import path
from . import views


# URL CONF !! issa route homes
urlpatterns = [
    path('hello/', views.say_hello)
]