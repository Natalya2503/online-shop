from django.db.models.base import Model as Model
from users.forms import UserLoginForm, UserRegistrationForm,UserProfileForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from users.forms import UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse


class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}
    success_url = reverse_lazy('main:index')

   

   
class RegisterUser(CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('user:login')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль пользователя'}

    def get(self,request, *args, **kvargs):

     response = super().get(request, *args, **kvargs)
     user = self.request.user
     response.set_cookie('user', user, max_age=3600)
     return response
    def get_extra_content(self, **kwargs):
     content = super().get_extra_content(**kwargs)
     cookie = self.request.COOKIES.get('user')
     content['cookies'] = cookie
     return content
   

    def get_success_url(self):
        return reverse_lazy('user:profile')
    
    def get_object(self, queryset=None):
      return self.request.user







