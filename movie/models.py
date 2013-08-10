from django.db import models
from taggit.managers import TaggableManager
from taggit.models import Tag,TaggedItemBase
from django.utils.translation import ugettext as _
from django_countries.fields import CountryField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from person.models import Person
from mediacontent.models import Album,VideoChannel
from lists.models import ListItem

class TaggedGenres(TaggedItemBase):
    	content_object = models.ForeignKey("Movie")

class TaggedKeywords(TaggedItemBase):
    	content_object = models.ForeignKey("Movie")

class MovieLanguages(TaggedItemBase):
    	content_object = models.ForeignKey("Movie")

class ProductionCompanies(TaggedItemBase):
    	content_object = models.ForeignKey("Movie")

class Movie(models.Model):
	title = models.CharField(_("Movie Title"),  
		max_length=128, help_text=_('Movie title exactly matching the title of movie when released in US'))
	plot = models.TextField(_("Plot/Summary"), help_text = _("Write a brief summary of the movie"))
	budget = models.FloatField(help_text=_("Budget in USD"))
	runtime = models.IntegerField(help_text=_("Run time in mins"))
	webpage = models.URLField(help_text=_("Official website of the movie"))

	genres = TaggableManager(through=TaggedGenres,verbose_name=_("Genres"),help_text=_("Comma separted values of genres the movie belongs to "))
    	genres.rel.related_name = "+genres"

	keywords = TaggableManager(through=TaggedKeywords,verbose_name=_("Keywords"),help_text = _("Comma separted values of important keywords related to movie"))
    	keywords.rel.related_name = "+keywords"

	languages = TaggableManager(through=MovieLanguages,verbose_name=_("Languages"),help_text=_("Comma separted values of all languages movie was relased in or languages in used movie"))
    	languages.rel.related_name = "+languages"

	production_companies = TaggableManager(through=ProductionCompanies,verbose_name=_("Production Companies"),help_text=_("Comma seprated values of all Production companies involved in this movie"))
    	production_companies.rel.related_name = "+production_companies"
	
	STATUS_OPTION = (
	('released','Released'),
	('scripting','Scripting'),
	('production','Production'),
	('rumour','Rumour'),
	)	

	status = models.CharField(choices=STATUS_OPTION,max_length=20,default="released",help_text=_("What's the current status of movie?"))
	objects = models.Manager() # The default manager.
	albums = generic.GenericRelation(Album)
	video_channels = generic.GenericRelation(VideoChannel)
	mlists = generic.GenericRelation(ListItem)
	class Meta:
		app_label = 'movie' 

	def __unicode__(self):
        	return '%s' % (self.title)

class Cast(models.Model):
	movie = models.ForeignKey(Movie,related_name="cast")
	person = models.ForeignKey(Person)
	character_name = models.CharField(max_length=128)
	def __unicode__(self):
        	return '%s:%s:%s' % (self.movie,self.person,self.character_name)

class Crew(models.Model):
	movie = models.ForeignKey(Movie,related_name="crew")
	person = models.ForeignKey(Person)
	job = models.CharField(max_length=128)
	
	def __unicode__(self):
        	return '%s:%s:%s' % (self.movie,self.person,self.job)

class Revenue(models.Model):
	movie = models.ForeignKey(Movie,related_name="revenue")
	country = CountryField("country",help_text="Choose country for the revenue")
	revenue = models.FloatField(help_text="Revenue till date, in USD") 
	def __unicode__(self):
        	return '%s:%s:%s' % (self.movie,self.country,self.revenue)

class ReleaseDate(models.Model):
	movie = models.ForeignKey(Movie,related_name="release_date")
	country = CountryField("country",help_text="Choose country")
	date = models.DateField(help_text="Release Date") 
	is_confirmed = models.BooleanField(help_text="Is this date confirmed?")
 	def __unicode__(self):
        	return '%s:%s:%s' % (self.movie,self.country,self.date)



