from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import context, loader
from django.urls import reverse

# Create your views here.

from .models import Question,Choice




def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join(q.question_text for q in latest_question_list)
    
    context={
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'pollman/index.html', context)
    # return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged
def detail(request, question_id):

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)
    
    context = {
        'question' : question,
    }

    return render(request, 'pollman/detail.html', context)



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'pollman/result.html', {'question': question})




def vote(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'pollman/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('pollman:results', args=(question.id,)))