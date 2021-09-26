from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):

    POSITION_LIST = [
        ("LECTURER", "LECTURER"),
        ("SENIOR_LECTURER", "SENIOR LECTURER"),
        ("HR", "HUMAN RESOURCES"),
    ]

    ROLE_LIST = [
        ("ADMIN", "ADMIN"),
        ("LECTURER", "LECTURER"),
        ("REVIEWER", "REVIEWER"),
        ("SDM_PT", "SDM PT")
    ]

    email = forms.EmailField(required = True)
    fullname = forms.CharField(required = True)
    university = forms.CharField(required = True)
    expertise = forms.CharField(required = True)
    position = forms.ChoiceField(choices = POSITION_LIST)
    role = forms.ChoiceField(choices = ROLE_LIST)

    class Meta:
	    model = User
	    fields = ("username", "email", "fullname", "password1", "password2", "university", "expertise", "position", "role")

    def save(self, commit=True):
	    user = super(NewUserForm, self).save(commit=False)
	    user.email = self.cleaned_data['email']

	    if commit:
		    user.save()
	    return user