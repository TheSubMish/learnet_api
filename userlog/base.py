from django.db import models

# choices for educational background
eduback_choices = (
    ("1","Higher Secondary"),
    ("2","Diploma or Certificate Programs"),
    ("3","Bachelor's Degree"),
    ("4","Master's Degree"),
    ("5","Doctoral Degree (Ph.D.)")
)

class UserBaseClass(models.Model):
    phone = models.CharField(blank=True, null=True,max_length=15)
    city = models.CharField(max_length=30,null=True)
    district = models.CharField(max_length=30,null=True)
    state = models.CharField(max_length=30,null=True)
    edubackground = models.CharField(max_length=30,choices=eduback_choices,default='1',null=True)

    class Meta:
        abstract = True