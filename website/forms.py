from django import forms
from .models import Contact,Newslatter

class ContactModelform(forms.ModelForm):
    class Meta:
        model = Contact
        fields ='__all__'
        

class NewslatterForm(forms.ModelForm):
    
    class Meta:
        model = Newslatter
        fields = '__all__'