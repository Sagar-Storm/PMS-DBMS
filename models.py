from django.db import models
from django.utils import timezone
import uuid
from django.core.validators import MinLengthValidator, RegexValidator
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User


name_regex = RegexValidator(regex=r'^[a-zA-Z\s]*$', message='Name should only contain characters')
phone_regex = RegexValidator(regex=r'^[789]\d{9}$', message='Invalid Phone Number')
register_regex = RegexValidator(regex=r'^1(RV|rv)\d{2}[a-zA-Z]{2}\d{3}$', message='Register Number is Invalid')





class Applicant(models.Model):
    Id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    FirstName = models.CharField(max_length = 30, validators = [name_regex])
    LastName = models.CharField(max_length = 30, validators = [name_regex])
    UserName = models.CharField(max_length = 30, validators = [name_regex], unique = True)
    MailId = models.EmailField(unique = True)
    Password = models.CharField(max_length = 25, validators = [MinLengthValidator(8)])
    PhoneNo = models.CharField(validators=[phone_regex], max_length=10)

    def __str__(self):
        return self.UserName

    class Meta:
        ordering = ["UserName"]
    
@receiver(post_save, sender=Applicant)
def save_p_user(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(username=instance.MailId, email=instance.MailId, password=instance.Password)
        user.profile.type = 'u'
    user.save()

@receiver(post_delete, sender=Applicant)
def delete_p_user(sender, instance, **kwargs):
    User.objects.filter(username=instance.MailId).delete()

class Application(models.Model):
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female')
    )

    CITIES = (
        ('ben', 'Bangalore'),
        ('mys', 'Mysore'),
        ('hub', 'Hubballi'),
        ('mdy', 'Mandya')
    )

    STATES = (
       ( 'ap', 'Andhra Pradesh'),
       ( 'mh', 'Maharashtra'),
        ('ka', 'Karnataka'),
    )


    ApplicantId = models.OneToOneField('Applicant', blank = False, null = False)
    FirstName = models.CharField(max_length = 30, validators = [name_regex], null = False, blank = False)
    MiddleName = models.CharField(max_length = 30, validators = [name_regex])
    LastName = models.CharField(max_length = 30, validators = [name_regex])
    DateOfBirth = models.DateField()
    Gender = models.CharField(max_length=10, choices = GENDER, default = 'm')
    FlatNo = models.CharField(max_length=15)
    State = models.CharField(max_length = 30, choices = CITIES, default='a')
    City = models.CharField(max_length = 30, choices = STATES , default='a')
    PlaceOfBirth = models.CharField(max_length = 30, blank = False, null = False)


class Documents(models.Model):
        ApplicantId = models.ForeignKey('Applicant', blank = False, null = False)
        AddressProof = models.FilePathField()
        BirthCertificate = models.FilePathField()
        PaymentReceipt = models.FilePathField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(default='u', max_length=1)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Status(models.Model):
    ApplicantId = models.OneToOneField('Applicant', blank = False, null = False)
    status = models.CharField(max_length = 500, blank = False, null = False)

