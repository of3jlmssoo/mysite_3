from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineField
from django.core.exceptions import ValidationError

# from django.contrib.admin.widgets import AdminDateWidget
# from .utils import OptionalChoiceField



# from people.models import Person
from app1.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('sw_name', 'sw_lic_id', 'sw_mnt_id', 'sw_not_use', 'sw_version', 'sw_quantity',
                 'sw_dev_comp', 'sw_lic_price', 'sw_mnt_price', 'sw_lic_date', 'sw_mnt_init_date', 'sw_mnt_update_date', 
                 'sw_sup_date', 'sw_in_charge', 'sw_vender_comp', 'sw_vender_rep', 'sw_vender_mail',
                 'sw_vender_tel','sw_installed','sw_other')
        sw_not_use = forms.BooleanField( label='sw_not_use', required=False, widget=forms.CheckboxInput(attrs={'class': 'check'}))

        # sw_lic_price = forms.DecimalField(label='sw_lic_price', localize=True)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))



# class OutPersonForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = ('name', 'email', 'job_title', 'bio', 'yourchoice1', 'yourchoice2', 'yourmultichoice')
#         yourchoice2 = forms.BooleanField( label='yourchoice2', required=False, widget=forms.CheckboxInput(attrs={'class': 'check'}))
#         yourchoice1 = forms.BooleanField( label='yourchoice1', required=False, widget=forms.CheckboxInput(attrs={'class': 'check'}))

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Save person'))
#         self.helper.layout = Layout(
#             InlineField('email', readonly=True),
#         )
