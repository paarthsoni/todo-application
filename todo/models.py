from django.db import models

# Create your models here.
class userdetails(models.Model):
    fname=models.CharField(max_length=122,null=True)
    lname=models.CharField(max_length=122,null=True)
    username=models.CharField(max_length=122,null=True)
    email=models.CharField(max_length=122,null=True)
    date=models.DateField(null=True)
    

    def __str__(self):
        return self.fname + " "+ self.lname


class tasks(models.Model):
    task=models.CharField(max_length=1024,null=False)
    username=models.CharField(max_length=122)
    date=models.DateTimeField()
    def __str__(self):
        return self.username
