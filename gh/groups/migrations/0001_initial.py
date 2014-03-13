# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Meetup'
        db.create_table(u'groups_meetup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('group_urlname', self.gf('django.db.models.fields.TextField')()),
            ('details', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'groups', ['Meetup'])


    def backwards(self, orm):
        # Deleting model 'Meetup'
        db.delete_table(u'groups_meetup')


    models = {
        u'groups.meetup': {
            'Meta': {'ordering': "['name']", 'object_name': 'Meetup'},
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'group_urlname': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['groups']