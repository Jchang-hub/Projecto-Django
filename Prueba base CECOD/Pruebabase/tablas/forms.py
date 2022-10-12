from django import forms 
from .models import Persona, choicepais
from datetime import date

class PersonaForm(forms.ModelForm):
    id              = forms.IntegerField()
    nombre          = forms.CharField(widget= forms.widgets.TextInput(attrs={'id': 'nombre'}))
    nacimiento      = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    paisp           = forms.ChoiceField(widget= forms.widgets.Select(attrs={'id': 'pais'}),choices = choicepais,label='Pais')
    nacionalidadp   = forms.CharField(widget= forms.widgets.TextInput(attrs={'id': 'nacionalidad'}),label='Nacionalidad')

    class Meta:
        model = Persona
        fields = [
            'id',
            'nombre',
            'nacimiento',
            'paisp',
            'nacionalidadp',
        ]

    def clean_nacimiento(self):
        nacimiento = self.cleaned_data['nacimiento']
        today = date.today()
        age = today.year - nacimiento.year - ((today.month, today.day) < (nacimiento.month, nacimiento.day))
        if not (age > 17):
            raise forms.ValidationError('No es mayor de 18')
        return nacimiento



