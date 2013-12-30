# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WebPage'
        db.create_table(u'sources_webpage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('selector', self.gf('django.db.models.fields.TextField')()),
            ('prefix', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'sources', ['WebPage'])


    def backwards(self, orm):
        # Deleting model 'WebPage'
        db.delete_table(u'sources_webpage')


    models = {
        u'sources.webpage': {
            'Meta': {'ordering': "['-title']", 'object_name': 'WebPage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'selector': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['sources']