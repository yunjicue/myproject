from django.db import models

# Create your models here.
#
class Additem(models.Model):
    itemname = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.itemname

class Info(models.Model):
    item = models.ForeignKey(Additem, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    contents = models.TextField()

    def __str__(self):
        return self.title
