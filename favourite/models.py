from django.db import models
from cloudinary.models import CloudinaryField


class Projects(models.Model):
    project_name = models.CharField(max_length=50)
    project_idea =models.TextField()
    project_front_image = CloudinaryField('image', default='image')



    def __str__(self):
        return self.project_name 


class Project_disc(models.Model):
    project_fdisc = models.TextField()
    project_github_link = models.URLField(max_length=1000000)
    project_deployed_link = models.URLField(max_length=1000000)
    projects = models.ForeignKey('Projects', on_delete=models.CASCADE)
    project_images = CloudinaryField('image', default='image')

    def __str__(self):
        return self.project_fdisc 