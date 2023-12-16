from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from stdimage import StdImageField
from stdimage.validators import MinSizeValidator

class Customuser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    email = models.EmailField(max_length=100, unique=True)
    surname = models.CharField(max_length=60)
    img = StdImageField(upload_to="images/", null=True, blank=True,
                    validators=[MinSizeValidator(540, 540)],
                    variations={
                        'md_crop': (540, 540, True),
                        'sm_crop': (270, 270, True)
                    },
                    delete_orphans=True,
                    verbose_name="Image de l'author",
                    )
