from django.db import models

# Create your models here.


class Paste(models.Model):
    LANG_CHOICES = (("Python", "Python"), 
                    ("JavaScript" , "JavaScript"), 
                    ("Outros", "Outros"))
    
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=50, choices=LANG_CHOICES)
    code = models.TextField()
