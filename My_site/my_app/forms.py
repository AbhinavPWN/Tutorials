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
        #fields = ['first_name', 'last_name', 'age']
        fields = '__all__'

        labels = {
            'first_name': 'Your name',
            'last_name': 'LAST name',
            'age': 'Your Age'
        }

        error_messages = {
            'age': {
                'min_value': 'The min value is 1',
                'max_value': 'The max value is 30'
            }
        }


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(
        max_length=500, required=False, widget=forms.Textarea)
