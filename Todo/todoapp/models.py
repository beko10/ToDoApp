from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100,verbose_name="Başlık")
    contex = models.TextField(verbose_name="İçerik")
    author = models.CharField(max_length=50,verbose_name="todo yazar")
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="oluşturulma tarihi")