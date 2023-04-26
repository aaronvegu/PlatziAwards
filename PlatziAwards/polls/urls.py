from django.urls import path

from . import views

# name to use it with url tag
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"), # send our CBV as views
    # ex: /polls/5 -> access to question with id 5
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results -> access to the answee to question with id 5
    path("<int:pk>/result", views.ResultView.as_view(), name="result"),
    # ex: /polls/5/vote -> access to vote for the question with id 5
    path("<int:question_id>/vote", views.vote, name="vote")
]