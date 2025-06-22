from django.contrib import admin

from .models import Taskgroup, Task, Project

admin.site.register(Project)
admin.site.register(Taskgroup)
admin.site.register(Task)