from django.db import models
from django.contrib.auth import get_user_model


class Project(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    description = models.CharField(
        max_length=256, blank=True, default='', verbose_name='descriptions')
    karma = models.IntegerField(default=0)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owner')
    participants = models.ManyToManyField(get_user_model())

    def __str__(self):
        return self.title


class ProjectComment(models.Model):
    commenter = models.ForeignKey(get_user_model(), blank=True, on_delete=models.PROTECT)
    project = models.ForeignKey(
        Project, on_delete=models.PROTECT, related_name='comments')  # wtf
    text = models.CharField(max_length=256)

    def __str__(self):
        return self.pk + text[:10]
