from django import forms

class ExampleForm(forms.Form):
    query = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search books...',
            'class': 'form-control'
        })
    )
