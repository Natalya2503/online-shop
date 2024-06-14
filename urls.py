from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('registration/', views.RegisterUser.as_view(), name='registration'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout')
]
