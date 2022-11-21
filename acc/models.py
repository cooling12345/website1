from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    comment = models.TextField()
    pic = models.ImageField(blank="True", upload_to='pic',default = '', null=True)
    email = models.EmailField(max_length=128, verbose_name="사용자 이메일")

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/noimage.png"
