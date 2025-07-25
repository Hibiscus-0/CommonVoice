from django.db.models import F
from django.shortcuts import *
from django.http import *
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# View for index
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

# View for detail
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

# View for results
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# View for vote
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request, 
            "polls/details.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else: 
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))

