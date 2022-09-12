from django.db import models


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField(null=True, blank=True)


class Comment(models.Model):
    meeting = models.ForeignKey('Meeting', on_delete=models.CASCADE, related_name='comments')
    description = models.TextField(max_length=3000)
