from django import forms


class AccountUserForm(forms.Form):
    username=forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'class': 'field_username'}

        ),

        label = 'Login',
        max_length=150
    )

    password = forms.CharField(
        max_length=250,
        widget = forms.widgets.PasswordInput(
            attrs={'class': 'field_password'}

        )
    )