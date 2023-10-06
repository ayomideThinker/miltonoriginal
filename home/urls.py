
from django.urls import path
from . import views 



urlpatterns = [
    path('', views.milton, name='milton'),
    path('sections/', views.sections, name='sections'),
    path('english/', views.english, name='english'),
    path('mathematics/', views.mathematics, name='mathematics'),
    path('economics/', views.economics, name='economics'),
    path('physics/', views.physics, name='physics'),
    path('signin/', views.signin, name='signin'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('profile_update/', views.signup, name='profile_update'),
    path('password/', views.signup, name='password'),
    path('logout_view/', views.logout_view, name='logout_view'),

]











