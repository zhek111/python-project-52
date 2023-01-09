from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from labels.forms import LabelCreateChangeForm
from labels.models import Label
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from statuses.views import CustomLoginRequiredMixin


class LabelsView(CustomLoginRequiredMixin, ListView):
    template_name = "labels/index.html"
    model = Label
    context_object_name = "labels"


class LabelsCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "labels/create.html"
    form_class = LabelCreateChangeForm
    success_url = '/labels'
    success_message = _("Labels created successfully")
    model = Label


class LabelsUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = LabelCreateChangeForm
    template_name = 'labels/update.html'
    success_url = '/labels'
    model = Label
    success_message = _("Labels changed successfully")


class LabelsDeleateView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'labels/delete.html'
    success_url = '/labels'
    model = Label
    success_message = _("Labels removed successfully")
    
    def dispatch(self, request, *args, **kwargs):
        label = self.get_object()
        if label.task_set.exists():
            messages.error(request,
                           _("Can't delete label because it's in use"))
            return redirect('list_labels')
        return super().dispatch(request, *args, **kwargs)

