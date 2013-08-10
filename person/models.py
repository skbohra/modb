from django.db import models

from django.utils.translation import ugettext as _
from django.contrib.contenttypes import generic
from mediacontent.models import Album
from lists.models import ListItem

class Person(models.Model):
        name = models.CharField(max_length=128,help_text=_('Name of the person'))
        biography = models.TextField(help_text=_('A short bio of the person'))
        birth_date = models.DateField(help_text=_('Birth date of the person'))
        death_date = models.DateField(help_text=_('If person is not alive, death date of the person'))
        place_of_birth = models.CharField(max_length=128,help_text=_('Native place of the person'))
        profile_pic = models.ImageField(upload_to='person',help_text=_('A nice pice of the person'))
        webpage = models.URLField(max_length=128,help_text=_('Official website of the person'))
	cover_pic = models.ImageField(upload_to='person',help_text=_('A cover pic for the person page'),null=True,blank=True,default=None)
	plists = generic.GenericRelation(ListItem)
	albums = generic.GenericRelation(Album)
	class Meta:
		app_label='person'

	def __unicode__(self):
                return '%s' % (self.name)


