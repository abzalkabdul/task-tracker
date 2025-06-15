from django.contrib import admin

from .models import Taskgroup, Task

admin.site.register(Taskgroup)
admin.site.register(Task)