# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Crew'
        db.create_table('movie_crew', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Movie'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['person.Person'])),
            ('job', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('movie', ['Crew'])

        # Adding model 'Image'
        db.create_table('movie_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Album'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.CharField')(default='poster', max_length=20)),
        ))
        db.send_create_signal('movie', ['Image'])

        # Adding model 'Cast'
        db.create_table('movie_cast', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Movie'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['person.Person'])),
            ('character_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('movie', ['Cast'])

        # Adding model 'Album'
        db.create_table('movie_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('movie', ['Album'])


    def backwards(self, orm):
        # Deleting model 'Crew'
        db.delete_table('movie_crew')

        # Deleting model 'Image'
        db.delete_table('movie_image')

        # Deleting model 'Cast'
        db.delete_table('movie_cast')

        # Deleting model 'Album'
        db.delete_table('movie_album')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'movie.album': {
            'Meta': {'object_name': 'Album'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'movie.cast': {
            'Meta': {'object_name': 'Cast'},
            'character_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['movie.Movie']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['person.Person']"})
        },
        'movie.crew': {
            'Meta': {'object_name': 'Crew'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['movie.Movie']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['person.Person']"})
        },
        'movie.image': {
            'Meta': {'object_name': 'Image'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['movie.Album']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'poster'", 'max_length': '20'})
        },
        'movie.movie': {
            'Meta': {'object_name': 'Movie'},
            'budget': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plot': ('django.db.models.fields.TextField', [], {}),
            'runtime': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'released'", 'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'webpage': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'movie.movielanguages': {
            'Meta': {'object_name': 'MovieLanguages'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['movie.Movie']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'movie_movielanguages_items'", 'to': "orm['taggit.Tag']"})
        },
        'movie.productioncompanies': {
            'Meta': {'object_name': 'ProductionCompanies'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['movie.Movie']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'movie_productioncompanies_items'", 'to': "orm['taggit.Tag']"})
        },
        'movie.taggedgenres': {
            'Meta': {'object_name': 'TaggedGenres'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['movie.Movie']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'movie_taggedgenres_items'", 'to': "orm['taggit.Tag']"})
        },
        'movie.taggedkeywords': {
            'Meta': {'object_name': 'TaggedKeywords'},
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['movie.Movie']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'movie_taggedkeywords_items'", 'to': "orm['taggit.Tag']"})
        },
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
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_items'", 'to': "orm['taggit.Tag']"})
        }
    }

    complete_apps = ['movie']