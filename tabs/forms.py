from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email Address', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea, max_length=400)
