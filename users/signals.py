from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
## create profile for each user automatically
# when a user is newly created
from django.core.exceptions import ObjectDoesNotExist

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    # try:
    #     instance.profile.save()
    # except ObjectDoesNotExist:
    #     Profile.objects.create(user=instance)
    ## Go to apps.py in user app to import users.signals

    # https://stackoverflow.com/questions/52244032/i-keep-getting-relatedobjectdoesnotexist-at-admin-login-how-do-i-successfully
