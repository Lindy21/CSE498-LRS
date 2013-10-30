# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field statements on 'Group'
        m2m_table_name = db.shorten_name('lrs_group_statements')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['lrs.group'], null=False)),
            ('statement', models.ForeignKey(orm['lrs.statement'], null=False))
        ))
        db.create_unique(m2m_table_name, ['group_id', 'statement_id'])

        # Deleting field 'Statement.group'
        db.delete_column('lrs_statement', 'group_id')


    def backwards(self, orm):
        # Removing M2M table for field statements on 'Group'
        db.delete_table(db.shorten_name('lrs_group_statements'))

        # Adding field 'Statement.group'
        db.add_column('lrs_statement', 'group',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lrs.Group'], null=True, on_delete=models.SET_NULL),
                      keep_default=False)


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lrs.activity': {
            'Meta': {'unique_together': "(('activity_id', 'global_representation'),)", 'object_name': 'Activity'},
            'activity_definition_choices': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'activity_definition_crpanswers': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'activity_definition_description': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'activity_definition_extensions': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'activity_definition_interactionType': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'activity_definition_moreInfo': ('django.db.models.fields.CharField', [], {'max_length': '2083', 'blank': 'True'}),
            'activity_definition_name': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'activity_definition_scales': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'activity_definition_sources': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'activity_definition_steps': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'activity_definition_targets': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'activity_definition_type': ('django.db.models.fields.CharField', [], {'max_length': '2083', 'blank': 'True'}),
            'activity_id': ('django.db.models.fields.CharField', [], {'max_length': '2083', 'db_index': 'True'}),
            'authoritative': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'global_representation': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'objectType': ('django.db.models.fields.CharField', [], {'default': "'Activity'", 'max_length': '8', 'blank': 'True'})
        },
        'lrs.activityprofile': {
            'Meta': {'object_name': 'ActivityProfile'},
            'activityId': ('django.db.models.fields.CharField', [], {'max_length': '2083', 'db_index': 'True'}),
            'content_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'etag': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json_profile': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'profile': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'profileId': ('django.db.models.fields.CharField', [], {'max_length': '2083', 'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'lrs.activitystate': {
            'Meta': {'object_name': 'ActivityState'},
            'activity_id': ('django.db.models.fields.CharField', [], {'max_length': '2083', 'db_index': 'True'}),
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lrs.Agent']"}),
            'content_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'etag': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json_state': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'registration_id': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'state': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'state_id': ('django.db.models.fields.CharField', [], {'max_length': '2083'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'lrs.agent': {
            'Meta': {'unique_together': "(('mbox', 'global_representation'), ('mbox_sha1sum', 'global_representation'), ('openID', 'global_representation'), ('oauth_identifier', 'global_representation'))", 'object_name': 'Agent'},
            'account_homePage': ('django.db.models.fields.CharField', [], {'max_length': '2083', 'blank': 'True'}),
            'account_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'global_representation': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mbox': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'db_index': 'True'}),
            'mbox_sha1sum': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'db_index': 'True'}),
            'member': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'member_rel_+'", 'null': 'True', 'to': "orm['lrs.Agent']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'oauth_identifier': ('django.db.models.fields.CharField', [], {'max_length': '192', 'null': 'True', 'db_index': 'True'}),
            'objectType': ('django.db.models.fields.CharField', [], {'default': "'Agent'", 'max_length': '6', 'blank': 'True'}),
            'openID': ('django.db.models.fields.CharField', [], {'max_length': '2083', 'null': 'True', 'db_index': 'True'})
        },
        'lrs.agentprofile': {
            'Meta': {'object_name': 'AgentProfile'},
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lrs.Agent']"}),
            'content_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'etag': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json_profile': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'profile': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'profileId': ('django.db.models.fields.CharField', [], {'max_length': '2083', 'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'lrs.consumer': {
            'Meta': {'object_name': 'Consumer'},
            'default_scopes': ('django.db.models.fields.CharField', [], {'default': "'statements/write,statements/read/mine'", 'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'secret': ('django.db.models.fields.CharField', [], {'default': "'aaC3dtGkXM'", 'max_length': '64'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'consumer_user'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'lrs.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'statements': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lrs.Statement']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        },
        'lrs.nonce': {
            'Meta': {'object_name': 'Nonce'},
            'consumer_key': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'token_key': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        'lrs.statement': {
            'Meta': {'object_name': 'Statement'},
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actor_statement'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['lrs.Agent']"}),
            'attachments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lrs.StatementAttachment']", 'symmetrical': 'False'}),
            'authority': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'authority_statement'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['lrs.Agent']"}),
            'context_extensions': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'context_instructor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'statement_context_instructor'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['lrs.Agent']"}),
            'context_language': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'context_platform': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'context_registration': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '40', 'blank': 'True'}),
            'context_revision': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'context_statement': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'context_team': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'statement_context_team'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['lrs.Agent']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'object_of_statement'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['lrs.Activity']"}),
            'object_agent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'object_of_statement'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['lrs.Agent']"}),
            'object_statementref': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'object_of_statement'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['lrs.StatementRef']"}),
            'object_substatement': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'object_of_statement'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['lrs.SubStatement']"}),
            'result_completion': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'result_duration': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'result_extensions': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'result_response': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'result_score_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'result_score_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'result_score_raw': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'result_score_scaled': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'result_success': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'statement_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '36', 'blank': 'True'}),
            'stored': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': "'2013-10-29T20:34:54.180843+00:00'", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'verb': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lrs.Verb']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0.0'", 'max_length': '7'}),
            'voided': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'})
        },
        'lrs.statementattachment': {
            'Meta': {'object_name': 'StatementAttachment'},
            'contentType': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'description': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'display': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'fileUrl': ('django.db.models.fields.CharField', [], {'max_length': '2083', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'payload': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'sha2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'usageType': ('django.db.models.fields.CharField', [], {'max_length': '2083'})
        },
        'lrs.statementcontextactivity': {
            'Meta': {'object_name': 'StatementContextActivity'},
            'context_activity': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lrs.Activity']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'statement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lrs.Statement']"})
        },
        'lrs.statementref': {
            'Meta': {'object_name': 'StatementRef'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_type': ('django.db.models.fields.CharField', [], {'default': "'StatementRef'", 'max_length': '12'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'lrs.substatement': {
            'Meta': {'object_name': 'SubStatement'},
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actor_of_substatement'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['lrs.Agent']"}),
            'context_extensions': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'context_instructor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'substatement_context_instructor'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['lrs.Agent']"}),
            'context_language': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'context_platform': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'context_registration': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '40', 'blank': 'True'}),
            'context_revision': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'context_statement': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'context_team': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'substatement_context_team'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['lrs.Agent']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'object_of_substatement'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['lrs.Activity']"}),
            'object_agent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'object_of_substatement'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['lrs.Agent']"}),
            'object_statementref': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'object_of_substatement'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['lrs.StatementRef']"}),
            'result_completion': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'result_duration': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'result_extensions': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'result_response': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'result_score_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'result_score_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'result_score_raw': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'result_score_scaled': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'result_success': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': "'2013-10-29T20:34:54.183058+00:00'", 'null': 'True', 'blank': 'True'}),
            'verb': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lrs.Verb']", 'null': 'True', 'on_delete': 'models.SET_NULL'})
        },
        'lrs.substatementcontextactivity': {
            'Meta': {'object_name': 'SubStatementContextActivity'},
            'context_activity': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lrs.Activity']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'substatement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lrs.SubStatement']"})
        },
        'lrs.token': {
            'Meta': {'object_name': 'Token'},
            'callback': ('django.db.models.fields.CharField', [], {'max_length': '2083', 'null': 'True', 'blank': 'True'}),
            'callback_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'consumer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lrs.Consumer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'lrs_auth_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'scope': ('django.db.models.fields.CharField', [], {'default': "'statements/write,statements/read/mine'", 'max_length': '100'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {'default': '1383078894L'}),
            'token_type': ('django.db.models.fields.SmallIntegerField', [], {'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tokens'", 'null': 'True', 'to': "orm['auth.User']"}),
            'verifier': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'lrs.verb': {
            'Meta': {'object_name': 'Verb'},
            'display': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'verb_id': ('django.db.models.fields.CharField', [], {'max_length': '2083', 'db_index': 'True'})
        }
    }

    complete_apps = ['lrs']