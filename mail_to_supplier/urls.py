from django.urls import path

from mail_to_supplier.views import NotificationTemplate
from mail_to_supplier.views import SendNotificationTemplate


urlpatterns = [

    path("supplier/notification/<int:id>", NotificationTemplate.as_view()),
    path("supplier/send/", SendNotificationTemplate.as_view())

]
