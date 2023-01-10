from django import forms
from users.models import User
from labels.models import Label
from django.forms import ModelForm
from statuses.models import Status
from tasks.models import Task
from django.utils.translation import gettext_lazy as _

class TaskCreateChangeForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']


class TaskFilterForm(forms.Form):
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=False,
        label=_("Status")
    )
    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label=_("Executor")
    )
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        required=False,
        label=_("Label")
    )
    only_my_tasks = forms.BooleanField(required=False,
                                       label=_("Only my tasks"))
