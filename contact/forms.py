from django import forms

class contactForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    phone = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea, required=True)