

from django.urls import path
from .import views
urlpatterns = [
    path('suggestionform', views.suggestionform, name='suggestionform'),
    
]
    
