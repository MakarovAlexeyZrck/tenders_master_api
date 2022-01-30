from django.urls import path

from phone_resurrection import views
from phone_resurrection.views import PhonesReestView

urlpatterns = [

    path(
        "resurrection/phone_state/<str:state>", views.fetch_on_phone_state),

    path(
        "resurrection/phone_update_status/<int:phone_update_status>",
        views.fetch_on_phone_update_status),

    path(
        "resurrection/update_phone_info/<int:phone_id>",
        PhonesReestView.as_view())

]
