from django.db import models
from dynamic_media import get_directory_path
from validators import validate_file_extension
from django.utils import timezone
import uuid
from datetime import datetime
import collections
from django.conf import settings

from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    name = models.CharField(max_length = 100, blank=True,null=True)                             
    mobile = models.CharField(max_length=15, blank=True, null=True)
    profile_img = models.FileField(upload_to=get_directory_path, blank=True,null=True)
    change_pass = models.BooleanField(default=True)
    password_to_know = models.CharField(max_length=200, blank=True, null=True)
    street_address = models.TextField(blank=True,null=True)
    zip_code = models.CharField(max_length=10,blank=True,null=True)
    city = models.CharField(max_length=20,blank=True,null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='u_created_by',
                                   blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='u_updated_by',
                                   blank=True, null=True)

    def __str__(self):
        return str(self.id)



