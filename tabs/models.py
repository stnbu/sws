from django.db import models

class Tab(models.Model):
    order = models.IntegerField()
    label = models.CharField(max_length=30)

class Content(models.Model):
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE)
    english = models.TextField()
    japanese = models.TextField()
