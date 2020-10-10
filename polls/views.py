from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
# Old Index -> 
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	template = loader.get_template('polls/index.html')
# 	context = {
# 		'latest_question_list':latest_question_list,
# 	}    
# 	return HttpResponse(template.render(context,request))

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {	'latest_question_list'	:	latest_question_list }
	return render(request,'polls/index.html',context)

# Old detail ->
# def detail(request,question_id):
# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404("Question Does not Exist")
# 	return render(request,'polls/details.html',{'question':question})

def detail(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request,'polls/details.html',{	'question'	:	question	})

def results(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request,'polls/result.html',{'question':question})

def vote(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		return render(request,'polls:detail.html',{
			'question':question,
			'error_message':'Choose an Option'
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))
#  reverse function helps avoid having to hardcode a URL in the view function.
#  It is given the name of the view that we want to pass control to and 
#  the variable portion of the URL pattern that points to that view.
#  reverse() call will return a string like
# '/polls/3/results/'