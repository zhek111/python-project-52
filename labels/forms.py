from django.forms import ModelForm
from labels.models import Label


class LabelCreateChangeForm(ModelForm):
    class Meta:
        model = Label
        fields = ['name']
