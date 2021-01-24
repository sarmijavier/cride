""" User model. """

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


#utilities
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """ User model. 
    
    Extends from Django's Abtract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed'
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=30,
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries.'
            'Clients are the main type of user.'   
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Change to true when the user has verified its email address.'
    )

