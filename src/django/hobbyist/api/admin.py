from django.contrib import admin
from hobbyist.api import models
# Register your models here.
admin.site.register(models.Project)
admin.site.register(models.ProjectComment)
