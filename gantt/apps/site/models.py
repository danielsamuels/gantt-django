from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Organisation(models.Model):

    name = models.CharField(
        max_length=100,
    )

    def __unicode__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, organisation, email_address, password, first_name, last_name):
        email_address = self.normalize_email(email_address)

        organisation = Organisation.objects.create(
            name=organisation
        )

        user = self.model(
            organisation=organisation,
            email_address=email_address,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, organisation, email_address, password, first_name, last_name):
        return self.create_user(organisation, email_address, password, first_name, last_name)


class User(AbstractBaseUser):

    objects = UserManager()

    organisation = models.ForeignKey(
        Organisation,
    )

    email_address = models.EmailField(
        unique=True,
    )

    first_name = models.CharField(
        max_length=100,
    )

    last_name = models.CharField(
        max_length=100,
    )

    USERNAME_FIELD = 'email_address'
    REQUIRED_FIELDS = ['organisation', 'password', 'first_name', 'last_name']

    def get_full_name(self):
        return u'{} {}'.format(
            self.first_name,
            self.last_name
        )

    def get_short_name(self):
        return u'{}'.format(
            self.first_name
        )

    def __unicode__(self):
        return u'{} {}'.format(
            self.first_name,
            self.last_name
        )


class Project(models.Model):

    organisation = models.ForeignKey(
        Organisation,
    )

    name = models.CharField(
        max_length=1000,
    )

    def __unicode__(self):
        return self.name


class TimelineItem(models.Model):

    project = models.ForeignKey(
        Project,
    )

    user = models.ForeignKey(
        User,
    )

    start_date = models.DateField()

    end_date = models.DateField()

    description = models.TextField(
        null=True,
    )
