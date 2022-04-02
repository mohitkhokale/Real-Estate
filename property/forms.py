from django import forms
from .models import Enquiry
class EnquiryForm(forms.ModelForm):

    state_choices = (
        ("1bhk","1 BHK"),
        ("2bhk","2 BHK"),
        ("3bhk","3 BHK"),
    )
    CHOICES = [('M','Male'),('F','Female')]
    requirement_type =forms.CharField(label='Requirement Type', widget=forms.RadioSelect(choices=state_choices))
    user_id = forms.CharField(widget = forms.HiddenInput(), required = False)
    user_name = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        model = Enquiry
        fields = ('enquiry_description','requirement_type','location','Budget','duration','property_type','questions','user_id','user_name')


