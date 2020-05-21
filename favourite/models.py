from django.db import models

# Create your models here.
class List(models:Model):
    project_name = models.CharField(max_length=50)
    project_image = models.ImageField(upload_to='', default='image to project')
    project_disc =models.TextField()



    def __str__(self):
        return self.project_name 


class project(models:Model):
    project_images = models.ImageField(upload_to='', default='image to project')
    project_fdisc = models.TextField()
    project_github_link = models.CharField()
    project_deployed_link = models.CharField()


    def __str__(self):
        return self.project_fdisc 