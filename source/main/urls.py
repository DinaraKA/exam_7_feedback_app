from django.contrib import admin
from django.urls import path
from webapp.views import PollIndexView, PollView, PollCreateView, PollUpdateView, PollDeleteView, \
    PollChoiceCreateView, ChoiceUpdateView, ChoiceDeleteView, AnswerPollChoiceCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollIndexView.as_view(), name='poll_index'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll_view'),
    path('poll/add/', PollCreateView.as_view(), name='poll_add'),
    path('poll/<int:pk>/update/', PollUpdateView.as_view(), name='poll_update'),
    path('poll/<int:pk>/delete/', PollDeleteView.as_view(), name='poll_delete'),
    path('poll/<int:pk>/choice_add/', PollChoiceCreateView.as_view(), name='poll_choice_create'),
    path('choice/<int:pk>/update/', ChoiceUpdateView.as_view(), name='choice_update'),
    path('choice/<int:pk>/delete/', ChoiceDeleteView.as_view(), name='choice_delete'),
    path('poll/answer/<int:pk>/', AnswerPollChoiceCreateView.as_view(), name='answer_choice_add')
]
