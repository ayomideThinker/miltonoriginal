from django.db import models
from django.contrib.auth.models import User
from quiz.models import *  # Assuming the model file is named 'quiz' and located in the same app

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='ad')
    last_name = models.CharField(max_length=100, default='ad')
    pix = models.ImageField(upload_to='Profile', default='avatar.jpg')
    email = models.EmailField()
    phone = models.CharField(max_length=100, default='ad')
    address = models.CharField(max_length=150, default='ad')
    dob = models.CharField(max_length=150, default='ad')
    # dob = models.DateField(auto_now_add=True)
    nationality = models.CharField(max_length=30, default='ad')
    gender = models.CharField(max_length=30, default='ad')
    state = models.CharField(max_length=50, default='ad')
    quiz_results = models.ManyToManyField(Question, through='QuizResult')

    def __str__(self):
        return self.user.username

class QuizResult(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.question.question_text}"
