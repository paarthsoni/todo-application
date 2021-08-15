from django.db import models

# Create your models here.
class userdetails(models.Model):
    fname=models.CharField(max_length=122)
    lname=models.CharField(max_length=122)
    username=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    date=models.DateField()
    

    def __str__(self):
        return self.fname + " "+ self.lname

class tasks(models.Model):
    tasks=models.CharField(max_length=1024)
    complete=models.BooleanField(default=True)
    

    def __str__(self):
        return self.tasks

