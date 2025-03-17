'''
from django.urls import path
from . import views

# Define your URL pattern(s) here
urlpatterns = [
    path('moving_square/', views.moving_square, name='moving_square'),
]
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='moving_square'),
]




