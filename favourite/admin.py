from django.contrib import admin

from .models import Projects, Project_disc



class ProjectDiscAdmin(admin.StackedInline):
    model = Project_disc

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjectDiscAdmin]

    class Meta:
        model = Projects

@admin.register(Project_disc)
class ProjectDiscAdmin(admin.ModelAdmin):
    pass