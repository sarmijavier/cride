""" Circle model. """


#Django
from django.db import models

#utilities
from cride.utils.models import CRideModel
import csv

class Circle(CRideModel):
    """ Circle model. 
    
    A circle is a private group where rides are offered and taken
    by its members. To join a circle a user must receive an unique
    invitation code from an existing circle member.
    
    """

    name = models.CharField('circle name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)


    about = models.CharField('circle description', max_length=255)
    picture = models.ImageField(upload_to='circles/pictures',blank=True, null=True)

    # Stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)
    
    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='Verified circles are also known as official communities.'
    )

    is_public = models.BooleanField(
        default=True,
        help_text='Public circles are listed in the main page so everyone know about their existence.'
    )
    
    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to fixed number of members.'
    )   

    members_limit = models.PositiveIntegerField(
        default=0,
        help_text='If circle is limited, this will be the limit on the number of members.'
    )

    def __str__(self):
        """ Return circle name. """
        return self.name
    
    class Meta(CRideModel.Meta):
        """ Meta class. """

        ordering = ['-rides_taken', '-rides_offered']




def data_from_csv(file):
    
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            if row[0] == 'name':
                pass
            else:
                circle = Circle(name=row[0], slug_name=row[1], is_public=row[2], verified=row[3], members_limit=row[4])
                circle.save()
