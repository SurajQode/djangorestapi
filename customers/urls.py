from django.urls import path
from . import views

urlpatterns = [
    # path('', views.customers_list),
    path('', views.CustomerList.as_view()),
    # path('<int:pk>', views.customer_details)
    path('<int:pk>', views.CustomerDetails.as_view())
]
