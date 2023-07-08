from flower_health_checks import views as healthcheck_views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('ping/', healthcheck_views.PingView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
