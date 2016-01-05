from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question,Choice
from django.template import RequestContext,loader
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([p.question_text for p in latest_question_list])
    # return HttpResponse(output)
    template = loader.get_template('py1/index.html')
    context = RequestContext(request,{'latest_question_list':latest_question_list})
    return HttpResponse(template.render(context))

def detail(request):
    template = loader.get_template('py1/detail.html')
    question = {'question_text':'aabbcc'}
    context = RequestContext(request,{'error_message':'jkljkl','question':question})
    return HttpResponse(template.render(context))

def vote(request):
    # p = get_object_or_404(Question,pk=question_id)
    # try:
    #     selected_choice = p.choice_set.get(pk=request.POST['choice'])
    # except (KeyError,Choice.DoesNotExist):
    #     return render(request,'poll.detail.html',{'question':p,'error_message':"you did't select a choice"})
    # else:
    # if(request.POST['choice']):
    #     return HttpResponse(request.POST['choice'])
    # elif(request.GET['choice']):
    #     return HttpResponse('elif:'+request.GET['choice'])
    # else:
    try:
        choice = request.POST['choice']
    except (KeyError):
        return HttpResponse('keyerror')
    else:
        return HttpResponse(choice)
def pytest(request):
    template = loader.get_template('py1/pytest.html')
    return HttpResponse(template.render())

