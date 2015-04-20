from django import forms
from . import models


class FolderForm(forms.Form):
    group_id = forms.CharField(max_length=100, label="group_id")
    author_id = forms.CharField(max_length=100, label="author_id")
    folder_name = forms.CharField(label="folder_name", max_length=100)
    parent = forms.CharField(max_length=100, label="parent", required=False)