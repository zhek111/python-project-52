from django.forms import ModelForm


from django.utils.translation import gettext as _

from labels.models import Labels


class LabelCreateChangeForm(ModelForm):
    class Meta:
        model = Labels
        fields = ['name']
