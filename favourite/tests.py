from django.test import TestCase
from .models import Projects, Project



class Projects(TestCase):
    def setUp(self):
        self.news = Projects(project_name = 'News', project_disc='a project to show moringa articles')

    def test_instance(self):
        self.assertTrue(isinstance(self.news,Projects))