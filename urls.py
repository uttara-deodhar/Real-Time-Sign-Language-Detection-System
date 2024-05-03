from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL for the index view
    path('detection/recognize_gesture_button/', views.recognize_gesture_button, name='recognize_gesture_button'),
]

