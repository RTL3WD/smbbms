"""erp URL Configuration

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

from .views import *

app_name = 'transactions'
urlpatterns = [
    # path('', payments.HomePageView.as_view(), name='home'),
    path('', index, name="index"),
    path('transaction/<int:transaction_id>', read_transaction, name="read-transaction"),
    path('settings/', transactions_settings,name="transactions-settings"),
    path('config/', payments.stripe_config),
    path('create-checkout-session/', payments.create_checkout_session),

    # path('point-of-sale/', transactions.point_of_sale, name="pos"),
    # path('checkout/',views.checkout,name="checkout"),
    # path('success/', payments.SuccessView.as_view()),
    # path('cancelled/', payments.CancelledView.as_view()),
    # path('webhook/', payments.stripe_webhook),
]

# FUNCTIONS
# Create Transaction
# Read Transaction
# Read All Transactions
# Update / Edit Transaction
# Delete Transaction
# Import Transaction
# Export Transaction

# PAGES
# Index
# Search Transactions
# Search Transactions Results
# Individual Transaction
# Individual Transaction Edit
# Create Transaction