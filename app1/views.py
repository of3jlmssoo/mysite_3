# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineField

from django.contrib.auth.models import User

from .filters import UserFilter

from django.http import HttpResponse
from .resources import PersonResource
import tablib
from tablib import Dataset



# Create your views here.
def index(request):
    print("======================================================================")
    return render(request, 'app1:index.html')

def redirect_view(request):
    response = redirect('/app1/')
    return response

###################################################################################    

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.shortcuts import redirect

# from people.models import Person
# from people.forms import PersonForm
from app1.models import Person
from app1.forms import PersonForm


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'

    def post(self, request):
        post_pks = request.POST.getlist('deletemultiple') 
        # Post.objects.filter(pk__in=post_pks).delete()
        Person.objects.filter(pk__in=post_pks).delete()
        return redirect('app1:person_list')  


class PersonCreateView(CreateView):
    template_name = "app1/person_form.html"
    model = Person
    fields = ('sw_name', 'sw_lic_id', 'sw_mnt_id', 'sw_not_use', 'sw_version', 'sw_quantity',
                'sw_dev_comp', 'sw_lic_price', 'sw_mnt_price', 
                'sw_lic_date', 'sw_mnt_init_date', 'sw_mnt_update_date', 'sw_sup_date', 
                'sw_banker', 
                'sw_vender_comp', 'sw_vender_rep', 'sw_vender_mail', 'sw_vender_tel',
                'sw_installed','sw_other')
    success_url = reverse_lazy('app1:person_list')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    # fields = ('name', 'email', 'job_title', 'bio', 'yourchoice1', 'yourchoice2','yourmultichoice')
    # fields = ('name', 'email', 'job_title', 'bio', )

    template_name = 'app1/person_update_form.html'
    success_url = reverse_lazy('app1:person_list')

    # def get(self, request, *args, **kwargs):
    #     print("===========================>", kwargs['pk'])
    



# class PersonUpdateView(UpdateView):
#     model = Person
#     form_class = PersonForm
#     # fields = ('name', 'email', 'job_title', 'bio', 'yourchoice1', 'yourchoice2','yourmultichoice')
#     # fields = ('name', 'email', 'job_title', 'bio', )

#     template_name = 'app1/person_update_form.html'
#     success_url = reverse_lazy('app1:person_list')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             'name',
#             InlineField('email', readonly=True),
#         )
        # self.helper.form_method = 'post'
        # self.helper.add_input(Submit('submit', 'Save person'))

class PersonDeleteView(DeleteView):
    model = Person
    # form_class = PersonForm
    success_url = reverse_lazy('app1:person_list')


def search(request):
    user_list = Person.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)

    print("==================== ",user_filter)

    # return render(request, 'search/user_list.html', {'filter': user_filter})
    return render(request, 'app1/search_list.html', {'filter': user_filter})


def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/json')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response


# def simple_upload(request):
#     if request.method == 'POST':
#         # person_resource = PersonResource()
#         # dataset = Dataset(headers = ['id','sw_name', 'sw_lic_id', 'sw_mnt_id', 'sw_not_use', 'sw_version', 'sw_quantity',
#         #          'sw_dev_comp', 'sw_lic_price', 'sw_mnt_price', 'sw_lic_date', 'sw_mnt_init_date', 'sw_mnt_update_date', 
#         #          'sw_sup_date', 'sw_banker', 'sw_vender_comp', 'sw_vender_rep', 'sw_vender_mail',
#         #          'sw_vender_tel','sw_installed','sw_other', 'version'])
#         # new_persons = request.FILES['myfile']

#         # print("=== simple_upload 1 ===")
#         # imported_data = dataset.load(new_persons.read())
#         # print("=== simple_upload 2 ===")
#         # result = person_resource.import_data(dataset, dry_run=True)  # Test the data import
#         # print("=== simple_upload 3 ===")

#         # if not result.has_errors():
#         #     person_resource.import_data(dataset, dry_run=False)  # Actually import now



#         print("=== simple_upload 1 ===")
#         person_resource = PersonResource()
#         print("=== simple_upload 2 ===")
#         new_persons = request.FILES['myfile']
#         print("=== simple_upload 3 ===")
#             # mydata = tablib.Dataset(headers=[ 'id', 'sw_name', 'sw_lic_id', 'sw_mnt_id', 'sw_not_use', 
#             #                 'sw_version', 'sw_quantity', 'sw_dev_comp', 'sw_lic_price', 'sw_mnt_price', 
#             #                 'sw_lic_date', 'sw_mnt_init_date', 'sw_mnt_update_date', 'sw_sup_date', 
#             #                 'sw_banker', 'sw_vender_comp', 'sw_vender_rep', 'sw_vender_mai', 'sw_vender_tel', 
#             #                 'sw_installed', 'sw_other', 'version', ]).load(open(new_persons ).read())
#         # mydata = tablib.Dataset(headers=[ 'id', 'sw_name', 'sw_lic_id', 'sw_mnt_id', 'sw_not_use', 
#         #                 'sw_version', 'sw_quantity', 'sw_dev_comp', 'sw_lic_price', 'sw_mnt_price', 
#         #                 'sw_lic_date', 'sw_mnt_init_date', 'sw_mnt_update_date', 'sw_sup_date', 
#         #                 'sw_banker', 'sw_vender_comp', 'sw_vender_rep', 'sw_vender_mai', 'sw_vender_tel', 
#         #                 'sw_installed', 'sw_other', 'version', ]).load(new_persons.read())
#         mydata = tablib.Dataset(headers=[ 'sw_name', 'sw_lic_id', 'sw_mnt_id', 'sw_not_use', 
#                         'sw_version', 'sw_quantity', 'sw_dev_comp', 'sw_lic_price', 'sw_mnt_price', 
#                         'sw_lic_date', 'sw_mnt_init_date', 'sw_mnt_update_date', 'sw_sup_date', 
#                         'sw_banker', 'sw_vender_comp', 'sw_vender_rep', 'sw_vender_mai', 'sw_vender_tel', 
#                         'sw_installed', 'sw_other' ]).load(new_persons.read())
#         print("=== simple_upload 4 ===")
#         result = person_resource.import_data(mydata, dry_run=True)
#         if not result.has_errors():
#             result = person_resource.import_data(mydata, dry_run=False)


#     return render(request, 'app1/simple_upload.html')

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'app1/simple_upload.html')