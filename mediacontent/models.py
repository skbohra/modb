from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext as _
from taggit.managers import TaggableManager

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Album(models.Model):
	content_type = models.ForeignKey(ContentType)
    	object_id = models.PositiveIntegerField()
    	content_object = generic.GenericForeignKey('content_type', 'object_id')
	title = models.CharField(_("Album Title"), max_length=256, help_text=_("A thoughtful title for this album"))

	def __unicode__(self):
                return '%s' % (self.title)


class VideoChannel(models.Model):
	content_type = models.ForeignKey(ContentType,blank=True,null=True)
    	object_id = models.PositiveIntegerField()
    	content_object = generic.GenericForeignKey('content_type', 'object_id')
	title = models.CharField(_("Channel Title"), max_length=256, help_text=_("A thoughtful title for this channel"))
	
	def __unicode__(self):
                return '%s' % (self.title)


class Video(models.Model): 
	channel = models.ForeignKey(VideoChannel,related_name="video",help_text=_("Choose a channel for this video"),blank=True,null=True) 
	source = models.URLField()
        title = models.CharField(max_length=256)	
	TYPE_OPTION = (
	('trailer','Trailer'),
	('teaser','Teaser'),
	('music','Music'),
	('interview','Interview'),
	)	
	alternate_source = models.URLField()
	type = models.CharField(choices=TYPE_OPTION,max_length=20,default="trailer",help_text=_("Video type?"))
    	tags = TaggableManager()
	from person.models import Person
	from movie.models import Movie
	

	movies_linked = models.ManyToManyField(Movie)
	person_linked = models.ManyToManyField(Person)

	def __unicode__(self):
                return '%s' % (self.title)

class Image(models.Model): 
	album = models.ForeignKey(Album,related_name="image",help_text=_("Choose an album for this image"),blank=True,null=True) 
	title = models.CharField(max_length="128",help_text="A nice title for the image")
	image = models.ImageField(upload_to="mediacontent",help_text=_("Choose an image to upload"))	
	thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})


	TYPE_OPTION = (
	('poster','Poster'),
	('wallpaper','Wallpaper'),
	('cover','Cover'),
	)	

	type = models.CharField(choices=TYPE_OPTION,max_length=20,default="poster",help_text=_("Image type?"))
    	tags = TaggableManager()
	from person.models import Person
	from movie.models import Movie
	

	movies_linked = models.ManyToManyField(Movie)
	person_linked = models.ManyToManyField(Person)

	def __unicode__(self):
                return '%s' % (self.image.url)



