import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

class QuestionMethodTests(TestCase):

	def test_was_published_recently_with_old_question(self):
		'''
		test_was_published_recently() shoild return false for question in the future
		'''
		time = timezone.now() + datetime.timedelta(days = 30)
		old_question = Question(pub_date=time)
		self.assertEqual(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
	    """
	    was_published_recently() should return True for questions whose
	    pub_date is within the last day.
	    """
	    time = timezone.now() - datetime.timedelta(hours=1)
	    recent_question = Question(pub_date=time)
	    self.assertEqual(recent_question.was_published_recently(), True)