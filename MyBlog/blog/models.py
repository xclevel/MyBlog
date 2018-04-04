from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.conf import settings
# Create your models here.

class ckeditorBlog(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=False)
    title = models.CharField(max_length=50, verbose_name="标题")
    content = RichTextUploadingField(blank=True, null=True, verbose_name="内容")

    def __unicode__(self):
        return self.name