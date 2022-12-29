from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from users.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import UserCreateChangeForm


class UsersView(ListView):
    template_name = "users/index.html"
    model = User
    context_object_name = "users"

class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = "users/create.html"
    form_class = UserCreateChangeForm
    success_url = '/login'
    success_message = "Пользователь создан"


class UserUpdateView(SuccessMessageMixin, UpdateView):
    form_class = UserCreateChangeForm
    template_name = 'users/update.html'
    success_url = '/users'
    model = User
    success_message = 'Обновилось успешно'
    
    def dispatch(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        if user != request.user:
            messages.error(request,
                           "У вас нет прав для изменения другого пользователя.")
            return redirect('list_users')

        return super().dispatch(request, *args, **kwargs)
    
    

class UserDeleateView(SuccessMessageMixin, DeleteView):
    template_name = 'users/delete.html'
    success_url = '/users/'
    model = User
    success_message = 'Удалилось'

    def dispatch(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        if user != request.user:
            messages.error(request,
                           "У вас нет прав для удаления другого пользователя.")
            return redirect('list_users')

        return super().dispatch(request, *args, **kwargs)