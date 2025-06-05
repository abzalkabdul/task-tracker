from django.contrib import admin

from task_tracker.core.models import Taskgroup, Task

admin.site.register(Taskgroup)
admin.site.register(Task)