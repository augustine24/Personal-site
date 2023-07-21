from django import forms

class ContactForm(forms.Form):
    sender_name = forms.CharField(max_length=100)
    sender_email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)