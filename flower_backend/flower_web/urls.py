from flower_web.api.goal import goal_views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('goals/', goal_views.GoalListView.as_view()),
    path('goals/<int:goal_id>/', goal_views.GoalDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
