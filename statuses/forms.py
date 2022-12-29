from django.forms import ModelForm

from statuses.models import Statuses
from django.utils.translation import gettext as _

class StatusCreateChangeForm(ModelForm):
    class Meta:
        model = Statuses
        fields = ['name']
