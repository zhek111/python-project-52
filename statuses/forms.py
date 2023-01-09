from django.forms import ModelForm
from statuses.models import Status


class StatusCreateChangeForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']
