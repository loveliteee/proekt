from typing import Any
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.urls import  reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import auth
from django.shortcuts import render
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import User


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
    context = {'form': form}
    context = {'form': UserLoginForm()}
    return render(request, 'users/login.html', context)


class UserLoginView( LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'


class UserRegistrationView( SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегестрированы!'
    title = 'Store - Регистрация'


def user_profile(request):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)

        user.username = request.POST.get("username")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")

        user.save()

        return render(request, 'users/profile.html', context={
            'message': "Изменения успешно сохранены!",
        })

    return render(request, 'users/profile.html')


class UserProfileUpdateView(UpdateView):
    model = User
    form_class = UserProfileForm
    queryset = User.objects.all()

    def get_success_url(self):
        messages.success(self.request, 'Данные профиля успешно обновлены.')
        return "/users/profile/%s"%self.get_object().pk






