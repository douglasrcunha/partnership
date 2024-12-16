from django.forms import ModelForm
from .models import Dashboard

class DasboardForm(ModelForm):
    class Meta:
        model = Dashboard
        fields = '__all__'
