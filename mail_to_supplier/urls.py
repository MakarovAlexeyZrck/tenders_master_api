from django.urls import path

from mail_to_supplier.views import NotificationSupplierRejection
from mail_to_supplier.views import NotificationSupplierTermination


urlpatterns = [

    path("supplier/rejection/", NotificationSupplierRejection.as_view()),
    path("supplier/termination/", NotificationSupplierTermination.as_view())

]
