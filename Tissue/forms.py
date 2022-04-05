from django import forms
from Tissue.models import database,Contact
class databaseForm(forms.ModelForm):
    class Meta:
        model=database
        fields={"title","description","name"}
    

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields={"name","lname","email","phone"}
