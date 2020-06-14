from django import forms



def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name',max_length=30)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message...', widget=forms.Textarea)
    forcefield = forms.CharField(required=False, widget=forms.HiddenInput, label='Leave Empty', validators=[should_be_empty])