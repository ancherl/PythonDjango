from django.db import models

# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='date published')

    # 魔法函数: 当print对象实例时， 自动触发此方法
    def __str__(self):
        return '(question_text=' + self.question_text + ', pub_date=' + str(self.pub_date) + ')'

class Choices(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return '(choice_text=' + self.choice_text + ', votes=' + str(self.votes) + ')'
