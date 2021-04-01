from import_export import resources
from .models import Person

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
        # fields = ('sw_name', 'sw_lic_id', 'sw_mnt_id', 'sw_not_use', 'sw_version', 'sw_quantity',
        #          'sw_dev_comp', 'sw_lic_price', 'sw_mnt_price', 'sw_lic_date', 'sw_mnt_init_date', 'sw_mnt_update_date', 
        #          'sw_sup_date', 'sw_in_charge', 'sw_vender_comp', 'sw_vender_rep', 'sw_vender_mail',
        #          'sw_vender_tel','sw_installed','sw_other')