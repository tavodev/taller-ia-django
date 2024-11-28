from django import forms


class ImageForm(forms.Form):
    image = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'form-control', 'accept': 'image/*'}
    ))
