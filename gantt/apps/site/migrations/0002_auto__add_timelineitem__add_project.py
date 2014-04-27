# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TimelineItem'
        db.create_table(u'site_timelineitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site.Project'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site.User'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'site', ['TimelineItem'])

        # Adding model 'Project'
        db.create_table(u'site_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['site.Organisation'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'site', ['Project'])


    def backwards(self, orm):
        # Deleting model 'TimelineItem'
        db.delete_table(u'site_timelineitem')

        # Deleting model 'Project'
        db.delete_table(u'site_project')


    models = {
        u'site.organisation': {
            'Meta': {'object_name': 'Organisation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'site.project': {
            'Meta': {'object_name': 'Project'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site.Organisation']"})
        },
        u'site.timelineitem': {
            'Meta': {'object_name': 'TimelineItem'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site.Project']"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site.User']"})
        },
        u'site.user': {
            'Meta': {'object_name': 'User'},
            'email_address': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['site.Organisation']"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['site']