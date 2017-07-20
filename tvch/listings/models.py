from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=200)
    number = models.DecimalField(max_digits=6, decimal_places=2) # Silly Digital TV with sub-channels
    logo = models.ImageField() # Might want to change this into a link...
    website = models.URLField()) # Not sure whether this should be schedule site or main website
    description = models.TextField()
    
