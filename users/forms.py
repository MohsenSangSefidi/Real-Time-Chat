from .models import Profile, User
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'image': forms.FileInput(),
            'nickname': forms.TextInput(attrs={'placeholder': 'Add display name'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Add bio'}),
        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']
