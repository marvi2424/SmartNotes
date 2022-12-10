from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["password"].widget.attrs.update({"class": "form-control"})


class CustomSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "id": "username"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "id": "password1"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "id": "password2"}
        )
