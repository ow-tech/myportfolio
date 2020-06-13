from django.db import models


class Projects(models.Model):
    project_name = models.CharField(max_length=50)
    project_disc =models.TextField()



    def __str__(self):
        return self.project_name 


class project_disc(models.Model):
    project = models.ForeignKey(Projects)
    project_fdisc = models.TextField()
    project_github_link = models.URLField(max_length=10000)
    project_deployed_link = models.URLField(max_length=10000)
    projects = models.ForeignKey('Projects', on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.project_fdisc 