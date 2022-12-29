from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from statuses.forms import StatusCreateChangeForm
from statuses.models import Statuses
from django.utils.translation import gettext
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class StatusView(LoginRequiredMixin, ListView):
    template_name = "statuses/index.html"
    model = Statuses
    context_object_name = "statuses"


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "statuses/create.html"
    form_class = StatusCreateChangeForm
    success_url = '/statuses'
    success_message = "Статус создан"
    model = Statuses


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = StatusCreateChangeForm
    template_name = 'statuses/update.html'
    success_url = '/statuses'
    model = Statuses
    success_message = 'Обновилось успешно'



class StatusDeleateView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'statuses/delete.html'
    success_url = '/statuses'
    model = Statuses
    success_message = 'Удалилось'
