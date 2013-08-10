# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ReleaseDate'
        db.create_table('movie_releasedate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Movie'])),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('is_confirmed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('movie', ['ReleaseDate'])


    def backwards(self, orm):
        # Deleting model 'ReleaseDate'
        db.delete_table('movie_releasedate')


    models = {
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
        'movie.releasedate': {
            'Meta': {'object_name': 'ReleaseDate'},
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['movie.Movie']"})
        },
        'movie.revenue': {
            'Meta': {'object_name': 'Revenue'},
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['movie.Movie']"}),
            'revenue': ('django.db.models.fields.FloatField', [], {})
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
            'cover_pic': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
        }
    }

    complete_apps = ['movie']