from django.db import models

CHOICE = (('danger', '高'),('warning', '中'),('primary','低'))

# Create your models here.
class TodoModel(models.Model):
  title = models.CharField(max_length=100)
  memo = models.TextField()
  priority = models.CharField(max_length=50,
                              choices = CHOICE
                              )
  duedate = models.DateField()

  def __str__(self):
    return self.title
    