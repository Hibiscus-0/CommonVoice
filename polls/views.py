from django.shortcuts import *
from django.http import HttpResponse
from .models import Question

# View for index
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


# View for detail
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {"question": question})


# View for results
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# View for vote
def vote(request, question_id):
    return HttpResponse("You're voting on a question %s." % question_id)

