# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'profiles_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('show_email', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('use_gravatar', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('info', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('skills', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('interested_in_job_opportunities', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('company', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('company_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('job_title', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('bitbucket_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('dribbble_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('facebook_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('github_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('google_plus_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('linked_in_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('stack_overflow_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('tumblr_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('twitter_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('project_1_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('project_1_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('project_2_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('project_2_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('project_3_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('project_3_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('project_4_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('project_4_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('project_5_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('project_5_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('elsewhere_1_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('elsewhere_1_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('elsewhere_2_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('elsewhere_2_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('elsewhere_3_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('elsewhere_3_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('elsewhere_4_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('elsewhere_4_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('elsewhere_5_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('elsewhere_5_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'profiles', ['Profile'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'profiles_profile')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'bitbucket_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'company': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'company_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'dribbble_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'elsewhere_1_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'elsewhere_1_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'elsewhere_2_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'elsewhere_2_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'elsewhere_3_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'elsewhere_3_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'elsewhere_4_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'elsewhere_4_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'elsewhere_5_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'elsewhere_5_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'facebook_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'github_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'google_plus_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'interested_in_job_opportunities': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_title': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'linked_in_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'project_1_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'project_1_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'project_2_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'project_2_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'project_3_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'project_3_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'project_4_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'project_4_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'project_5_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'project_5_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'show_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'skills': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'stack_overflow_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'tumblr_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'use_gravatar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['profiles']