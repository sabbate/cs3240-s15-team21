from django import forms
<<<<<<< HEAD
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
=======
from . import models


class FolderForm(forms.Form):
    group_id = forms.CharField(max_length=100, label="group_id")
    author_id = forms.CharField(max_length=100, label="author_id")
    folder_name = forms.CharField(label="folder_name", max_length=100)
    parent = forms.CharField(max_length=100, label="parent", required=False)
>>>>>>> 1406712f6d54d1138114cc3a031b342503d235f7
