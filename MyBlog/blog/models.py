from ckeditor.fields import RichTextField
from django.db import models
from django.conf import settings
# Create your models here.

class Blog(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=False)
    title = models.CharField(max_length=50, verbose_name="标题")
    content = RichTextField(blank=True, null=True, verbose_name="内容")

    def __unicode__(self):
        return self.name