from django.db import models
import uuid


class BaseClass(models.Model):
    uuid = models.SlugField(default=uuid.uuid4, unique=True)
    active_status = models.BooleanField(default=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class FormModel(BaseClass):
    field1=models.CharField(max_length=255)
    field2=models.CharField(max_length=255)
    field3=models.CharField(max_length=255)


    def  __str__(self):
        return f"Form-{self.id}" 

    class Meta:
        ordering = ['-id']
        verbose_name = 'Form'
        verbose_name_plural = 'Form'