from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')   #jakie pola należy uwzględnić w formularzu


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())

    def clean_name(self):
        data = self.cleaned_data['name']
        if "D" not in data:
            raise forms.ValidationError("Imię musi zawierać 'D'!")
        return data