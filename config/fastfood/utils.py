from django.db import models


class DataInfo(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)