from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from enterprenour.models import *


# Create your models here.
class InvestorDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_min = models.IntegerField()
    amount_max = models.IntegerField()
    industries = models.ManyToManyField(Industry)
    location = models.ManyToManyField(Location)
    background_info = models.TextField()
    experiencing_area = models.TextField()

    def __str__(self):
        return f"{self.user.first_name} | {self.user.email}"

    class Meta:
        verbose_name = 'InvestorDetail'
        verbose_name_plural = 'InvestorDetails'


class ProjectAssignment(models.Model):
    user = models.ForeignKey(InvestorDetail, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignment_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user.user.first_name} | {self.user.user.email}"

    class Meta:
        verbose_name = 'ProjectAssignment'
        verbose_name_plural = 'ProjectAssignments'
