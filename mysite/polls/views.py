#from django.http import Http404
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

#from django.template import RequestContext, loader

from .models import Choice, Question

class IndexView(generic.ListView):
	template_name = 'polls/index.html' 
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions"""
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk= request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		#redisplay the question voting form
		return render(request, 'polls/detail.html', {
			'question':p, 
			'error_message': "You didn't select a choice",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()

	return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


	#return HttpResponse("You are voting on question %s." %question_id)










#Initial code without generic views

#def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# 	# Without the render() shortcut
# 	# #output =', '.join([p.question_text for p in latest_question_list])
# 	# template = loader.get_template('polls/index.html')
# 	# context = RequestContext(request, {
# 	# 	'latest_question_list': latest_question_list,
# 	# 	})
# 	# return HttpResponse(template.render(context))
	
# 	#return HttpResponse(output)

# 	#return HttpResponse("Hello world.Your are at polls index!")
	
	
# def detail(request, question_id):
#  #    try:
#  #        question = Question.objects.get(pk=question_id)
#  #    except Question.DoesNotExist:
#  #        raise Http404("Question does not exist")
#  #    return render(request, 'polls/detail.html', {'question': question})
# 	# #return HttpResponse("You are looking at the question %s ." % question_id)

# 	#get_object_or_404
	
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def vote(request, question_id):
# 	p = get_object_or_404(Question,pk=question_id)
# 	try:
# 		selected_choice = p.choice_set.get(pk= request.POST['choice'])
# 	except (KeyError, Choice.DoesNotExist):
# 		#redisplay the question voting form
# 		return render(request, 'polls/detail.html', {
# 			'question':p, 
# 			'error_message': "You didn't select a choice",
# 			})
# 	else:
# 		selected_choice.votes += 1
# 		selected_choice.save()

# 	return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


# 	#return HttpResponse("You are voting on question %s." %question_id)
# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/results.html', {'question':question})

# 	#response = "You are looking at the results of question %s " 
# 	#return HttpResponse(response % question_id)
