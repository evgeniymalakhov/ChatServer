from django import forms
from chat.models import Message


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ""}
