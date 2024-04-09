from django.db.models import TextChoices


class UserGroupChoices(TextChoices):
    ADMIN = "Admin"