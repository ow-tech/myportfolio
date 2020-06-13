from django.db import models
from cloudinary.models import CloudinaryField


class Projects(models.Model):
    project_name = models.CharField(max_length=50)
    project_idea =models.TextField()
    project_github_link = models.URLField(max_length=1000000, default='github link')
    project_deployed_link = models.URLField(max_length=1000000, default='deployed link')
    project_front_image = CloudinaryField('image', default='image')



    def __str__(self):
        return '{},{}'.format(self.project_name, self.project_idea)


class Project_disc(models.Model):
    projects = models.ForeignKey('Projects', on_delete=models.CASCADE)
    project_images = CloudinaryField('image', default='image')

    def __str__(self):
        return self.projects.project_name