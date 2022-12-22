
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin


from users.models import User
from django.views.generic.edit import CreateView, UpdateView
from .forms import UserCreateForm, UserUpdateForm


class UsersView(ListView):
    template_name = "users/index.html"
    model = User
    context_object_name = "users"

class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = "users/update.html"
    form_class = UserCreateForm
    success_url = '/login'
    success_message = "Пользователь создан"
    

from django.views.generic import UpdateView

from django.views.generic.edit import UpdateView

class UserUpdateView(UpdateView):
    template_name = "users/update.html"
    form_class = UserUpdateForm
    success_url = '/login'
    success_message = "Пользователь обновлен"
    model = User
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)