import uuid

from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.user.managers import CustomUserManager

from utils.constants import UserGroupChoices

class CustomUserGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        _("name"),
        choices=UserGroupChoices.choices,
        max_length=100,
    )
    permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("permissions"),
        related_name="permissions",
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    middle_name = models.CharField(
        _("middle name"), max_length=64, blank=True, null=True
    )
    username = None
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    groups = models.ManyToManyField(
        CustomUserGroup,
        help_text=_(
            "The group this user belongs to. The user will be able to perform "
            "all actions according to respective permissions."
        ),
        verbose_name=_("groups"),
        blank=True,
        related_name="users",
        related_query_name="user",
    )

    objects = CustomUserManager()

    @property
    def get_full_name(self) -> str:
        return (
            f"{self.first_name} {self.middle_name} {self.last_name}"
            if self.middle_name
            else f"{self.first_name} {self.last_name}"
        )

    def __str__(self) -> str:
        return self.email