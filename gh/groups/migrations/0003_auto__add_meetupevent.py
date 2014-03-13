# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MeetupEvent'
        db.create_table(u'groups_meetupevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meetup', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['groups.Meetup'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('venue_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('address_1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('address_2', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('address_3', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('city', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('state', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('zip_code', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('event_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'groups', ['MeetupEvent'])


    def backwards(self, orm):
        # Deleting model 'MeetupEvent'
        db.delete_table(u'groups_meetupevent')


    models = {
        u'groups.meetup': {
            'Meta': {'ordering': "['name']", 'object_name': 'Meetup'},
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'group_urlname': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'next_event_json': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'next_event_updated_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'groups.meetupevent': {
            'Meta': {'object_name': 'MeetupEvent'},
            'address_1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'address_2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'address_3': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'event_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'meetup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['groups.Meetup']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'state': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'venue_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'zip_code': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['groups']