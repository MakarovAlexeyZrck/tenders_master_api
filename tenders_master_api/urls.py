from django.urls import path, include


urlpatterns = [
    path("mail/", include("mail_to_supplier.urls")),
    path("templates/", include("html_templates.urls")),
    path("phones/", include("phone_resurrection.urls")),
]
