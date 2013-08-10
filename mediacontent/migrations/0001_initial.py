# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table('mediacontent_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('mediacontent', ['Album'])

        # Adding model 'Image'
        db.create_table('mediacontent_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mediacontent.Album'], null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('type', self.gf('django.db.models.fields.CharField')(default='poster', max_length=20)),
        ))
        db.send_create_signal('mediacontent', ['Image'])

        # Adding M2M table for field movies_linked on 'Image'
        m2m_table_name = db.shorten_name('mediacontent_image_movies_linked')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('image', models.ForeignKey(orm['mediacontent.image'], null=False)),
            ('movie', models.ForeignKey(orm['movie.movie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['image_id', 'movie_id'])

        # Adding M2M table for field person_linked on 'Image'
        m2m_table_name = db.shorten_name('mediacontent_image_person_linked')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('image', models.ForeignKey(orm['mediacontent.image'], null=False)),
            ('person', models.ForeignKey(orm['person.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['image_id', 'person_id'])

        # Adding model 'VideoChannel'
        db.create_table('mediacontent_videochannel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('mediacontent', ['VideoChannel'])

        # Adding model 'Video'
        db.create_table('mediacontent_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mediacontent.Album'], null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('alternate_source', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(default='trailer', max_length=20)),
        ))
        db.send_create_signal('mediacontent', ['Video'])

        # Adding M2M table for field movies_linked on 'Video'
        m2m_table_name = db.shorten_name('mediacontent_video_movies_linked')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['mediacontent.video'], null=False)),
            ('movie', models.ForeignKey(orm['movie.movie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['video_id', 'movie_id'])

        # Adding M2M table for field person_linked on 'Video'
        m2m_table_name = db.shorten_name('mediacontent_video_person_linked')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['mediacontent.video'], null=False)),
            ('person', models.ForeignKey(orm['person.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['video_id', 'person_id'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table('mediacontent_album')

        # Deleting model 'Image'
        db.delete_table('mediacontent_image')

        # Removing M2M table for field movies_linked on 'Image'
        db.delete_table(db.shorten_name('mediacontent_image_movies_linked'))

        # Removing M2M table for field person_linked on 'Image'
        db.delete_table(db.shorten_name('mediacontent_image_person_linked'))

        # Deleting model 'VideoChannel'
        db.delete_table('mediacontent_videochannel')

        # Deleting model 'Video'
        db.delete_table('mediacontent_video')

        # Removing M2M table for field movies_linked on 'Video'
        db.delete_table(db.shorten_name('mediacontent_video_movies_linked'))

        # Removing M2M table for field person_linked on 'Video'
        db.delete_table(db.shorten_name('mediacontent_video_person_linked'))


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mediacontent.album': {
            'Meta': {'object_name': 'Album'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'mediacontent.image': {
            'Meta': {'object_name': 'Image'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mediacontent.Album']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'movies_linked': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['movie.Movie']", 'symmetrical': 'False'}),
            'person_linked': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['person.Person']", 'symmetrical': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'poster'", 'max_length': '20'})
        },
        'mediacontent.video': {
            'Meta': {'object_name': 'Video'},
            'alternate_source': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mediacontent.Album']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movies_linked': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['movie.Movie']", 'symmetrical': 'False'}),
            'person_linked': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['person.Person']", 'symmetrical': 'False'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'trailer'", 'max_length': '20'})
        },
        'mediacontent.videochannel': {
            'Meta': {'object_name': 'VideoChannel'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
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

    complete_apps = ['mediacontent']