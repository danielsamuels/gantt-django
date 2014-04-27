from django import forms
from .models import User, Organisation

class UserCreationForm(forms.ModelForm):
    organisation = forms.CharField(
        label="Organisation name"
    )

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])

        organisation_name = self.cleaned_data['organisation']
        organisation = Organisation.objects.create(
            name=organisation_name
        )

        user.organisation = organisation

        if commit:
            user.save()
        return user

    class Meta:
        model = User
        exclude = ['last_login']
        fields = ['first_name', 'last_name', 'email_address', 'password']
