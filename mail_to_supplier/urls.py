from django.urls import path

from mail_to_supplier.views import NotificationTemplate


urlpatterns = [

    path("supplier/notification/<int:id>", NotificationTemplate.as_view()),

]
