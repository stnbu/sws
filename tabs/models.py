from django.db import models

class Tab(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=30)
    label = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Content(models.Model):
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE)
    english = models.TextField(blank=True)
    japanese = models.TextField(blank=True)

    def __str__(self):
        return self.tab.name
