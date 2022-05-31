"""BMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from products.views.app_settings import app_settings

from .views import *


app_name = 'contacts'
urlpatterns = [
    path('', index , name="index"),
    path('add/', add_contact, name="add-contact"),
    path('contact/<int:pk>/', GetContactDetailView.as_view(), name="get-contact"),
    path('contact/<int:id>/config/', stripe_config),
    path('contact/<int:id>/checkout/', stripe_config),
    path('contact/<int:cid>/phone/add', add_contact_phone, name="add-contact-phone"), 
    path('contact/<int:cid>/phone/<int:pid>/delete/', del_contact_phone, name="delete-contact-phone"), 
    path('contact/<int:pk>/update/', update_contact, name="update-contact"), 
    path('search-contacts/', search_contacts, name="search-contacts"),
    path('search-results/', search_results, name="search-results"),
    path('settings/', contacts_settings ,name="contacts-settings"),
    # path('create-checkout-session/', contacts_settings ,name="contacts-settings"),
]
