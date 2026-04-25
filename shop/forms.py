from django.forms import ModelForm
from .models import CommissionRequest


class CommissionForm(ModelForm):
    class Meta:
        model = CommissionRequest
        fields = ['name', 'email', 'occasion', 'recipient', 'details', 'language', 'budget']
