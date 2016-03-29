from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import *

from geographies.models import District

class UserModelDistrictMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.district_name)

class QaCocoUserForm(forms.ModelForm):
    districts = UserModelDistrictMultipleChoiceField(
        widget=FilteredSelectMultiple(
                                      verbose_name='districts',
                                      is_stacked=False
                                     ),
        queryset=District.objects.all()
        )
    