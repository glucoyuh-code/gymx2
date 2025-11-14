from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'gender', 'address', 'phone', 'membership']
        widgets = {
            'membership': forms.Select(
                attrs={'class': 'form-control'},
                choices=Customer._meta.get_field('membership').choices
            ),
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address', 'gender', 'membership']
        widgets = {
            'gender': forms.RadioSelect(choices=Customer.GENDER_CHOICES),
            'membership': forms.Select(choices=Customer.MEMBERSHIP_CHOICES),
        }