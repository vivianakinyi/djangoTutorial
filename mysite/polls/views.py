#from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#output =', '.join([p.question_text for p in latest_question_list])
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'latest_question_list': latest_question_list,
		})
	return HttpResponse(template.render(context))


	#return HttpResponse(output)
		

	#return HttpResponse("Hello world.Your are at polls index!")

def detail(request,question_id):
	return HttpResponse("You are looking at the question %s ." % question_id)

def results(request, question_id):
	response = "You are looking at the results of question %s " 
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You are voting on question %s." %question_id)