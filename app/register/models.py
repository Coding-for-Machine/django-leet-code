from django.contrib.auth.models import AbstractBaseUser , BaseUserManager, PermissionsMixin, Group
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        """Create and return a 'CustomUser ' with an email, username, and password."""
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)  # Use set_password to hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """Create and return a superuser with an email, username, and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Required for admin access
    date_joined = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Specify a unique related_name for the groups field
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Unique related name
        blank=True,
        help_text='Ushbu foydalanuvchi tegishli bo\'lgan guruhlar.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Unique related name
        blank=True,
        help_text='Foydalanovchi ro\'xsatnomalari!.',
        verbose_name='Fofoydalanuvch ro\'xsatnomalari!',
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']  # Add any other required fields here

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")



# class Article(models.Model):
#     def image_upload_to(self, instance=None):
#         if instance:
#             return os.path.join('ArticleSeries', slugify(self.series.slug), slugify(self.article_slug), instance)
#         return None

#     ...
#     image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to, max_length=255)