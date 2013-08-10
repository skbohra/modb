# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductionCompanies'
        db.create_table('movie_productioncompanies', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='movie_productioncompanies_items', to=orm['taggit.Tag'])),
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Movie'])),
        ))
        db.send_create_signal('movie', ['ProductionCompanies'])

        # Adding model 'MovieLanguages'
        db.create_table('movie_movielanguages', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='movie_movielanguages_items', to=orm['taggit.Tag'])),
            ('content_object', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Movie'])),
        ))
        db.send_create_signal('movie', ['MovieLanguages'])

        # Adding field 'Movie.status'
        db.add_column('movie_movie', 'status',
                      self.gf('django.db.models.fields.CharField')(default='released', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ProductionCompanies'
        db.delete_table('movie_productioncompanies')

        # Deleting model 'MovieLanguages'
        db.delete_table('movie_movielanguages')

        # Deleting field 'Movie.status'
        db.delete_column('movie_movie', 'status')


    models = {
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
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['movie']