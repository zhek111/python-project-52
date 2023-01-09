from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from users.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import UserCreateChangeForm
from django.utils.translation import gettext_lazy as _


class UsersView(ListView):
    template_name = "users/index.html"
    model = User
    context_object_name = "users"


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = "users/create.html"
    form_class = UserCreateChangeForm
    success_url = '/login'
    success_message = _('User successfully registered')


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = UserCreateChangeForm
    template_name = 'users/update.html'
    success_url = '/users'
    model = User
    success_message = _('User changed successfully')
    login_url = '/login/'
    redirect_field_name = 'next'

    def dispatch(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        if not request.user.is_authenticated:
            messages.error(request,
                           "You are not authorized! Please sign in.")
        elif user != request.user:
            messages.error(request, _('You do not have permission '
                                      'to change another user'))
            return redirect('list_users')
        return super().dispatch(request, *args, **kwargs)


class UserDeleateView(SuccessMessageMixin, DeleteView):
    template_name = 'users/delete.html'
    success_url = '/users/'
    model = User
    success_message = _('User deleted successfully')

    def dispatch(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        if not request.user.is_authenticated:
            messages.error(request,
                           "You are not authorized! Please sign in.")
            return redirect('login')
        elif user != request.user:
            messages.error(request,
                           _('You do not have permission to delete another '
                             'user'))
            return redirect('list_users')
        elif user.tasks_author.exists() or user.tasks_executor.exists():
            messages.error(request,
                           _('Unable to delete user because he used'))
            return redirect('list_users')
        return super().dispatch(request, *args, **kwargs)
