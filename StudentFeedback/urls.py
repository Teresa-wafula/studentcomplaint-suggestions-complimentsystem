

from django.urls import path
from .import views
urlpatterns = [
    path('',views.index, name='index' ),
    path('register',views.register, name='register' ),
    path('login',views.login, name='login' ),
    path('complaintform',views.complaintform, name='complaintform' )
]
