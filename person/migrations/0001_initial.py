# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('person_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('biography', self.gf('django.db.models.fields.TextField')()),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('death_date', self.gf('django.db.models.fields.DateField')()),
            ('place_of_birth', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('profile_pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('webpage', self.gf('django.db.models.fields.URLField')(max_length=128)),
        ))
        db.send_create_signal('person', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('person_person')


    models = {
        'person.person': {
            'Meta': {'object_name': 'Person'},
            'biography': ('django.db.models.fields.TextField', [], {}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'death_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'place_of_birth': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'profile_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'webpage': ('django.db.models.fields.URLField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['person']