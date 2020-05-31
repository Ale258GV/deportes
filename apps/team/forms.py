from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    #Formulario para registrar alumnos


    class Meta:
        model = Student
        #fields = '__all__'
        exclude = ('liberado',)
        labels = {
            'team':''
        }
        widgets = {
            'team':forms.NumberInput(attrs={'hidden':True})
        }

