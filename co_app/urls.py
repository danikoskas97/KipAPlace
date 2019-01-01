from django.urls import path
from . import views

app_name = 'co_app'

urlpatterns = [
path('', views.index, name='index'),
path('signup/', views.signup, name='signup'),
path('login/', views.login_auth, name='login_auth'),
path('logout_auth/', views.logout_auth, name='logout_auth'),
path('profile/<int:user_id>/', views.profile, name='profile')
]


  
