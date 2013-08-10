# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TaggedGenres'
        db.create_table('movie_taggedgenres', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='movie_taggedgenres_items', to=orm['taggit.Tag'])),
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Movie'])),
        ))
        db.send_create_signal('movie', ['TaggedGenres'])

        # Adding model 'TaggedKeywords'
        db.create_table('movie_taggedkeywords', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='movie_taggedkeywords_items', to=orm['taggit.Tag'])),
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Movie'])),
        ))
        db.send_create_signal('movie', ['TaggedKeywords'])

        # Adding model 'Movie'
        db.create_table('movie_movie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('plot', self.gf('django.db.models.fields.TextField')()),
            ('budget', self.gf('django.db.models.fields.FloatField')()),
            ('runtime', self.gf('django.db.models.fields.IntegerField')()),
            ('webpage', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('movie', ['Movie'])


    def backwards(self, orm):
        # Deleting model 'TaggedGenres'
        db.delete_table('movie_taggedgenres')

        # Deleting model 'TaggedKeywords'
        db.delete_table('movie_taggedkeywords')

        # Deleting model 'Movie'
        db.delete_table('movie_movie')


    models = {
        'movie.movie': {
            'Meta': {'object_name': 'Movie'},
            'budget': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plot': ('django.db.models.fields.TextField', [], {}),
            'runtime': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'webpage': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['movie']