from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Profile
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView
from .forms import ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms

class ProductListView(ListView):
    model = Product  # Указываем, с какой моделью работает представление
    template_name = 'shop/product_list.html'  # Путь к шаблону
    context_object_name = 'products'  # Как будет называться список в шаблоне

class RegisterView(CreateView):
    template_name = 'shop/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('product_list')  

class UserLoginView(LoginView):
    template_name = 'shop/login.html'  # Шаблон для формы входа

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('product_list')  # После выхода перенаправляем на главную страницу

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address', 'profile_picture']  # Убрали bio

class ProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'shop/profile.html'
    # Устанавливаем ссылку для редиректа после сохранения
    success_url = reverse_lazy('profile')

    def get_object(self):
        # Получаем профиль текущего пользователя, если он существует, или создаем новый
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile