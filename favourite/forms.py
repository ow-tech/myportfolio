from django import forms

class ContactForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
    message = forms.Textarea(lebel='message...')