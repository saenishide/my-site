from django.db import models

# Model = データベースの定義
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    todayWord = models.TextField('today word', max_length=140, blank=True)
    imgUrl = models.CharField('image url', max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    deleteFlag = models.BooleanField(default=False)
    def __str__(self):
        return self.title