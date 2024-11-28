from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Configurare uniformă pentru toate câmpurile
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.label = ''
            if field_name == 'username':
                field.widget.attrs['placeholder'] = 'User Name'
                field.help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
            elif field_name == 'password1':
                field.widget.attrs['placeholder'] = 'Password'
                field.help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
            elif field_name == 'password2':
                field.widget.attrs['placeholder'] = 'Confirm Password'
                field.help_text = ''





class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget= forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label = "")
    last_name = forms.CharField(required=True, widget= forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label = "")
    email =forms.CharField(required=True, widget= forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label = "")
    phone =forms.CharField(required=True, widget= forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label = "")
    address =forms.CharField(required=True, widget= forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label = "")
    city =forms.CharField(required=True, widget= forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label = "")
    state =forms.CharField(required=True, widget= forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label = "")
    zipcode =forms.CharField(required=True, widget= forms.widgets.TextInput(attrs={"placeholder":"ZipCode", "class":"form-control"}), label = "")

    class Meta:
        model = Customer
        exclude = ["user",]