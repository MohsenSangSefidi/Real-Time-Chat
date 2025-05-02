from django import forms
from .models import GroupMessages


class CreateMessageForm(forms.ModelForm):
    class Meta:
        model = GroupMessages
        fields = ['body']
        widgets = {
            'body': forms.TextInput(
                attrs={
                    'placeholder': 'Write message ...',
                    'class': 'p-4 text-black',
                    'maxlength': '300',
                    'autofocus': True
                }
            ),
        }
