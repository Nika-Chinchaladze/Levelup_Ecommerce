from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserImage


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={"placeholder": "Username", "class": "form-control"}), label="", required=True)
    password = forms.CharField(
        max_length=150, widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}), label="", required=True)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    email = forms.EmailField(max_length=150, required=False)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",
                  "email", "password1", "password2",)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields["first_name"].label = ""
        self.fields["last_name"].label = ""
        self.fields["username"].label = ""
        self.fields["email"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""

        self.fields["first_name"].widget.attrs["placeholder"] = "First name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Last name"
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["password1"].widget.attrs["placeholder"] = "Password 1"
        self.fields["password2"].widget.attrs["placeholder"] = "Password 2"

        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"

        self.fields["username"].max_length = 150
        self.fields["password1"].max_length = 150
        self.fields["password2"].max_length = 150


class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ("image",)

    def __init__(self, *args, **kwargs):
        super(UserImageForm, self).__init__(*args, **kwargs)

        self.fields["image"].label = ""
