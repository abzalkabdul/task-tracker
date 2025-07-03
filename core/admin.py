from django.contrib import admin
from django.utils.text import slugify

from .models import Taskgroup, Task, Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    exclude = ('slug',)

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            base_slug = slugify(obj.name)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            obj.slug = slug
        super().save_model(request, obj, form, change)
        
admin.site.register(Taskgroup)
admin.site.register(Task)