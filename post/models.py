from distutils.command.upload import upload
from django.db import models
from user.models import UserModel


class PostModel(models.Model):

    class Meta:
        db_table = 'post'

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=256)
    photo = models.ImageField('상품', upload_to='iterms', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
