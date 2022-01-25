from distutils.command.upload import upload
from django.db import models
from user.models import UserModel


class PostModel(models.Model):

    class Meta:
        db_table = 'post'

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=256)
    photo = models.URLField(("상품이미지"), max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
