from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateField('date published')

	def __str__(self):
		return '{} on {}'.format(self.question_text,self.pub_date)
	
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_txt = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return '{} on {}'.format(self.choice_txt,self.votes)
