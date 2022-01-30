from django.urls import path

from phone_resurrection import views

urlpatterns = [

    path(
        "resurrection/phone_state/<str:state>",
        views.fetch_on_phone_state
    ),

    path(
        "resurrection/phone_update_status/<int:phone_update_status>",
        views.fetch_on_phone_update_status
    ),

]
