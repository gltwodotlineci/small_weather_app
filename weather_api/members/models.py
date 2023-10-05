from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Customuser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    email = models.EmailField(max_length=100, unique=True)
    surname = models.CharField(max_length=60)
