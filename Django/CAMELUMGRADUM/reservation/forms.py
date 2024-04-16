from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from .models import Reserve

class ReserveForm(ModelForm):
    class Meta:
        model = Reserve
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set widget for RDate field to use DateInput
        self.fields['RDate'].widget = forms.DateInput(attrs={'type': 'date'})
        # Set widget for RTime field to use TimeInput
        self.fields['RTime'].widget = forms.TimeInput(attrs={'type': 'time'})
        # Remove labels for all fields
        for field_name in self.fields:
            self.fields[field_name].label = False
        # Add placeholder text for fields
        self.fields['RName'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['RDate'].widget.attrs['placeholder'] = 'Reservation Date'
        self.fields['RTime'].widget.attrs['placeholder'] = 'Reservation Time'
        self.fields['RPersons'].widget.attrs['placeholder'] = 'Number of Persons'