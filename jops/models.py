from django.db import models

# Create your models here.
# Django Models are
#   Validtions and html weight 

JOB_TYPE = (
    ('Full-Time','Full-Time'),
    ('Part-Time','Part-Time'),
)

class Job(models.Model): #table
    titel       = models.CharField(max_length=100) #colume
    jop_type    = models.CharField(max_length=20,default='FullTime',choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published   = models.DateTimeField(auto_now = True)
    Vacany      = models.IntegerField(default=1)
    salary      = models.IntegerField(default=0)
    experience  = models.IntegerField(default=1)

    def __str__(self):
        return self.titel
 

