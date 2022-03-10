from django.urls import path
from . import views

urlpatterns=[
    path('index/', views.index, name='index'),
    path('<str:room_name>/', views.room, name='rooms'),
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]