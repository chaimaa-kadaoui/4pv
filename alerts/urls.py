from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from alerts import views

urlpatterns = [
    url(r"^alerts/$", views.AlertList.as_view()),
    url(r"^alerts/(?P<pk>[0-9]+)/$", views.AlertDetail.as_view()),
    url(r"^alerts-active/$", views.ActiveAlertDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
