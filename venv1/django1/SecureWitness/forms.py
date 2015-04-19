from django import forms


class FolderForm(forms.Form):
    folder_name = forms.CharField(label="folder_name", max_length=100)