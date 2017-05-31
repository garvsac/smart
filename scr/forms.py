from scr.models import Category
from django import forms

Department = (
    ('rma','R.M.A.'),
    ('production', 'Production'),
    ('warehouse', 'Warehouse'),
    ('maintenance', 'Maintenance'),
)

Type = (
    ('hazardous', 'Hazardous'),
    ('e-waste', 'e-Waste'),
    ('metals', 'Metals'),
    ('paper', 'Paper'),
    ('plastic', 'Plastic'),
)

class MyModelForm(forms.ModelForm):
    department = forms.ChoiceField(choices=Department,required=True,
                                    help_text="Department")
    waste_type = forms.ChoiceField(choices=Type, required=True,
                                    help_text="Type of Waste")
    description = forms.CharField(max_length=1000,
                                    help_text="Description")
    class Meta:
        model = Category
        fields = ['department', 'waste_type', 'description']
