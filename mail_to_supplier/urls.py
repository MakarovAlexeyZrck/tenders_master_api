from django.urls import path

from mail_to_supplier.views import NotificationTemplate
from mail_to_supplier.views import SendNotificationTemplate

from mail_to_supplier.views import NotificationSupplierRejection
from mail_to_supplier.views import NotificationSupplierTermination
urlpatterns = [

    path("supplier/notification/<int:id>", NotificationTemplate.as_view()),
    path("supplier/send/", SendNotificationTemplate.as_view()),

    path(
        "supplier/rejection/",
        NotificationSupplierRejection.as_view()
    ),

    path(
        "supplier/termination/",
        NotificationSupplierTermination.as_view()
    )

]
