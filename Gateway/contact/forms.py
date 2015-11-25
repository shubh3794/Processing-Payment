from django import forms

class contactForm(forms.Form):
	name = forms.CharField(max_length=100, required = True, help_text = 'Fill in your name' )
	email = forms.EmailField(required = True)
	comment = forms.CharField(required = True, widget=forms.Textarea)