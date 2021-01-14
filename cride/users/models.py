""" User model. """

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser


#utilities
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """ User model. 
    
    Extends from Django's Abtract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(_
        'email address',
        unique=True,
        error_message={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_number = models.CharField(
        max_length=30,
        blank=True
    )
