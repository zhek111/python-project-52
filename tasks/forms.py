from django import forms
from users.models import User
from labels.models import Labels
from django.forms import ModelForm

from statuses.models import Statuses
from tasks.models import Tasks

class TaskCreateChangeForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'status', 'executor', 'labels']

class TaskFilterForm(forms.Form):
    status = forms.ModelChoiceField(
        queryset=Statuses.objects.all(),
        required=False,
        label='Статус'
    )
    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label='Исполнитель'
    )
    labels = forms.ModelMultipleChoiceField(
        queryset=Labels.objects.all(),
        required=False,
        label='Метки'
    )
    only_my_tasks = forms.BooleanField(required=False, label='Только мои задачи')
