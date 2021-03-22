from django.contrib import admin
from django.urls import path
from . import views
from app1.views import PersonListView, PersonCreateView, PersonUpdateView, PersonDeleteView
from django.conf.urls import url

# from django_filters.views import FilterView
from .models import Person

app_name ="app1"

urlpatterns = [
    path('person_add/', PersonCreateView.as_view(), name='person_add'),
    path('', PersonListView.as_view(), name='person_list'),
    path('person_list/', PersonListView.as_view(), name='person_list'),
    path('<int:pk>/edit/', PersonUpdateView.as_view(), name='person_edit'),
    path('<int:pk>/delete/', PersonDeleteView.as_view(), name='delete'),
    # path('search/', views.search, name='search'),
    # url(r'^search/$', FilterView.as_view(model=Person)),
    url(r'^search/$', views.search, name='search_list' ),
    url(r'^export/$', views.export, name='export'),
    url(r'^simple_upload/$', views.simple_upload, name='simple_upload'),


]
