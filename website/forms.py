from django import forms
from .models import Contact,Newslatter
from captcha.fields import CaptchaField

class ContactModelform(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields ='__all__'
        
        

class NewslatterForm(forms.ModelForm):
    
    class Meta:
        model = Newslatter
        fields = '__all__'