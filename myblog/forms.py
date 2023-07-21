from django import forms

class ContactForm(forms.Form):
    sender_name = forms.CharField(max_length=300, required=True)
    sender_email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=300, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)