from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField(blank=True,null=-True)
    completed=models.BooleanField(False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title