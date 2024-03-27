

from django.urls import path
from .import views
from Suggestions import views as suggestionviews
from Compliments import views as complimentviews
urlpatterns = [

    path('',views.index, name='index' ),
    path('register',views.register, name='register' ),
    path('login',views.login, name='login' ),
    path('complaintform',views.submit_complaint, name='complaintform' ),
    path('suggestionform',suggestionviews.suggestionform, name='suggestionform'),
    path('complimentform', complimentviews.compliment, name='complimentform')

    # path('error', suggestionviews.error, name='error')

    # path('suggestionform', views.sugg, name='')
]
