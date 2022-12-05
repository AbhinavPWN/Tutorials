from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please give your Feedback', max_length=200,
#                              widget=forms.Textarea(attrs={'class': 'review1', 'id': 'review1'}))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'age']
