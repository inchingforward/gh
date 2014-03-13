# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Meetup.next_event_json'
        db.add_column(u'groups_meetup', 'next_event_json',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Meetup.next_event_updated_date'
        db.add_column(u'groups_meetup', 'next_event_updated_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Meetup.next_event_json'
        db.delete_column(u'groups_meetup', 'next_event_json')

        # Deleting field 'Meetup.next_event_updated_date'
        db.delete_column(u'groups_meetup', 'next_event_updated_date')


    models = {
        u'groups.meetup': {
            'Meta': {'ordering': "['name']", 'object_name': 'Meetup'},
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'group_urlname': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'next_event_json': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'next_event_updated_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['groups']