

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from labels.forms import LabelCreateChangeForm
from labels.models import Labels

from django.views.generic.edit import CreateView, UpdateView, DeleteView


class LabelsView(LoginRequiredMixin, ListView):
    template_name = "labels/index.html"
    model = Labels
    context_object_name = "labels"


class LabelsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "labels/create.html"
    form_class = LabelCreateChangeForm
    success_url = '/labels'
    success_message = "Метка создан"
    model = Labels


class LabelsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = LabelCreateChangeForm
    template_name = 'labels/update.html'
    success_url = '/labels'
    model = Labels
    success_message = 'Обновилось успешно'



class LabelsDeleateView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'labels/delete.html'
    success_url = '/labels'
    model = Labels
    success_message = 'Удалилось'
