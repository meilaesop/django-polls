from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='questions')
    
    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    @property
    def total_votes(self):
        """计算该问题的总投票数"""
        return sum(choice.votes for choice in self.choice_set.all())
    
    @property
    def is_owner(self, user):
        """检查用户是否是问题的创建者"""
        return self.author == user

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    """记录用户投票的模型"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='user_votes')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='user_choices')
    vote_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'question')  # 每个用户对每个问题只能投一次票
    
    def __str__(self):
        return f"{self.user.username} voted for {self.choice.choice_text} in {self.question.question_text}"
