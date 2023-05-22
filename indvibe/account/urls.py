from django.urls import path
from .import views
urlpatterns = [
    path('',views.index),
    path('index2',views.index2,name='index2'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('contact',views.contact,name='contact'),
    path('signuppage', views.signuppage, name='signuppage'),
    path('signinpage', views.signinpage, name='signinpage'),
    path('userhome',views.userhome, name='userhome'),
    path('contactuspage', views.contactuspage, name='contactuspage'),
    path('logout', views.logout,name='logout'),

]
