from django.urls import path

from phone_resurrection.views import PhonesReestView


urlpatterns = [

    path("resurrection/", PhonesReestView.as_view()),
    path("resurrection/<int:id>", PhonesReestView.as_view()),

]
