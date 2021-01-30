from django.db import models


def handle_upload_to(instance, filename):
    return '{}/{}'.format(instance.uid, filename)


class File(models.Model):
    uid = models.CharField(max_length=200)
    file = models.FileField(upload_to=handle_upload_to)
