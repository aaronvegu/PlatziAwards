import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    # columns
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # string function
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # columns
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # string function
    def __str__(self):
        return self.choice_text