from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext as _
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class MList(models.Model):
	title = models.CharField(_("List Title"), max_length=256, help_text=_("A thoughtful title for this list"))
	description = models.TextField(_("List description"), help_text=_("A brief description for this list"))
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

class ListItem(models.Model):
	content_type = models.ForeignKey(ContentType)
    	object_id = models.PositiveIntegerField()
    	content_object = generic.GenericForeignKey('content_type', 'object_id')
	mlist = models.ForeignKey(MList,related_name="mlist")	
	def __unicode__(self):
		return self.mlist.title


