from django.urls import path

from mail_to_supplier.views import MailToSupplier


urlpatterns = [

    path("supplier/", MailToSupplier.as_view())

]
