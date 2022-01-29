from django.urls import path

from html_templates.views import RejectionTemplate
from html_templates.views import TerminationTemplate


urlpatterns = [

    path("rejection/", RejectionTemplate.as_view()),
    path("termination/", TerminationTemplate.as_view())

]
