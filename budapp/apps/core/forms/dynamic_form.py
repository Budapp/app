from django import forms


class DynamicForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
