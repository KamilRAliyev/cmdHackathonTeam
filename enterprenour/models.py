from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Location(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'


class Industry(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = 'Industry'
        verbose_name_plural = 'Industries'


class Stage(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = 'Stage'
        verbose_name_plural = 'Stages'


class Team(models.Model):
    team_overview = models.TextField()

    def __str__(self):
        return f"{self.team_overview}"

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class TeamMembers(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(upload_to='visa/e_visa', null=True, blank=True)

    def __str__(self):
        return f"{self.name}|{self.team}"

    class Meta:
        verbose_name = 'TeamMember'
        verbose_name_plural = 'TeamMembers'


class InvestorRole(models.Model):
    role = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.role}"

    class Meta:
        verbose_name = 'InvestorRole'
        verbose_name_plural = 'InvestorRoles'


# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=50)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    investor_role = models.ForeignKey(InvestorRole, on_delete=models.CASCADE)
    min = models.IntegerField(default=0)
    max = models.IntegerField()

    def __str__(self):
        return f"{self.title}|{self.user}"

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'



class ProjectDetails(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    short_summary = models.TextField()
    business_idea = models.TextField()
    market = models.TextField()
    proof = models.TextField()
    objectives = models.TextField()
    tags = models.TextField()

    def __str__(self):
        return self.project.title

    class Meta:
        verbose_name = "ProjectDetail"
        verbose_name_plural = "ProjectDetails"
