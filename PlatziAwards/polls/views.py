from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

## Function Based Views - DRY PRINCIPLE
# def index(request):
#     # query all question in database
#     latest_question_list = Question.objects.all()
#     # return render func with 3 params: request, view url, dict of variables
#     return render(request, "polls/index.html", {
#         "latest_question_list": latest_question_list
#     })

# def detail(request, question_id):
#     # get question with corresponding id
#     # using get_object_or_404 we provide 2 params: Object to query, query
#     question = get_object_or_404(Question, pk=question_id)
#     # return question with render
#     return render(request, "polls/detail.html", {
#         "question": question
#     })

# def result(request, question_id):
#     # get question voted
#     question = get_object_or_404(Question, pk=question_id)
#     # return to results template with the obtained question
#     return render(request, "polls/result.html", {
#         "question": question
#     })



# we get an request and question_id from our form on detail.html, that redirects to vote view
def vote(request, question_id):
    # get Question from question.id with our 404 funct to get errors
    question = get_object_or_404(Question, pk=question_id)
    # if the response exists
    try:
        # obtain the selected choice from form, where name is the option
        # where our user response is on a POST dict with, particularly, the choice opt in choice key
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist): #if it does not exists
        # render func needs a request, template to render and context as params
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    else: # if its turn well
        # add one to the votes to our question selected
        selected_choice.votes += 1
        # save our model
        selected_choice.save()
        # we redirect our user to another page, with Redirect we make sure users don't send the form twice
        # reverse() is the way to write a url tag in Python
        # reverse() receives the url to redirect, and tupla args to make work the url define on urls.py/results
        return HttpResponseRedirect(reverse("polls:result", args=(question_id, )))