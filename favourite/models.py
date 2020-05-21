from django.db import models

# Create your models here.
class Projects(models.Model):
    project_name = models.CharField(max_length=50)
    # project_image = models.ImageField(upload_to='', default='image to project')
    project_disc =models.TextField()



    def __str__(self):
        return self.project_name 


class Project(models.Model):
    # project_images = models.ImageField(upload_to='', default='image to project')
    project_fdisc = models.TextField()
    project_github_link = models.CharField(max_length=10000)
    project_deployed_link = models.CharField(max_length=10000)
    projects = models.ForeignKey('Projects', on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.project_fdisc 