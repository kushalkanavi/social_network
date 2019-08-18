from django import forms
from .models import UserProfile, GENDER


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

        fields = [
            'firstname',
            'lastname',
            'age',
            'gender',
            'location',
            'photo',
            'interests',
        ]

        labels = {
            'firstname': 'First Name',
            'lastname'	: 'Last Name',
            'age'			: 'Age',
            'gender'		: 'Gender',
            'location'	: 'Location',
            'photo'		: 'Photo',
            'interests'		: 'Interests',
        }

        widgets = {
            'firstname': forms.TextInput(attrs={'name': 'firstname', 'class': 'form-control', 'placeholder': 'First Name', }),
            'lastname': forms.TextInput(attrs={'name': 'lastname', 'class': 'form-control', 'placeholder': 'Last Name', }),
            'age': forms.TextInput(attrs={'name': 'vendor', 'class': 'form-control', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'name ': 'gender ', 'class ': 'form-control ', 'placeholder ': 'Gender'}),
            'location': forms.TextInput(attrs={'name ': 'location ', 'class ': 'form-control ', 'placeholder ': 'Location'}),
            'photo': forms.FileInput(attrs={'type ': 'date ', 'name ': 'batchdate ', 'class ': 'form-control ', 'placeholder ':'Batch_Date'}),
            'interests': forms.TextInput(attrs={'name ': 'interests ', 'class ': 'form-control ', 'placeholder ': 'Interest'}),

        }
