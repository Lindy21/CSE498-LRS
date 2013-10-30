# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Nonce'
        db.create_table('lrs_nonce', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('token_key', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('consumer_key', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('lrs', ['Nonce'])

        # Adding model 'Consumer'
        db.create_table('lrs_consumer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('default_scopes', self.gf('django.db.models.fields.CharField')(default='statements/write,statements/read/mine', max_length=100)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('secret', self.gf('django.db.models.fields.CharField')(default='XmcWLpsnnG', max_length=64)),
            ('status', self.gf('django.db.models.fields.SmallIntegerField')(default=1)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='consumer_user', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal('lrs', ['Consumer'])

        # Adding model 'Token'
        db.create_table('lrs_token', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('secret', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('token_type', self.gf('django.db.models.fields.SmallIntegerField')(db_index=True)),
            ('timestamp', self.gf('django.db.models.fields.IntegerField')(default=1382587275L)),
            ('is_approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('lrs_auth_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='tokens', null=True, to=orm['auth.User'])),
            ('consumer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lrs.Consumer'])),
            ('scope', self.gf('django.db.models.fields.CharField')(default='statements/write,statements/read/mine', max_length=100)),
            ('verifier', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('callback', self.gf('django.db.models.fields.CharField')(max_length=2083, null=True, blank=True)),
            ('callback_confirmed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('lrs', ['Token'])

        # Adding model 'Verb'
        db.create_table('lrs_verb', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('verb_id', self.gf('django.db.models.fields.CharField')(max_length=2083, db_index=True)),
            ('display', self.gf('jsonfield.fields.JSONField')(blank=True)),
        ))
        db.send_create_signal('lrs', ['Verb'])

        # Adding model 'Agent'
        db.create_table('lrs_agent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('objectType', self.gf('django.db.models.fields.CharField')(default='Agent', max_length=6, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('mbox', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, db_index=True)),
            ('mbox_sha1sum', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, db_index=True)),
            ('openID', self.gf('django.db.models.fields.CharField')(max_length=2083, null=True, db_index=True)),
            ('oauth_identifier', self.gf('django.db.models.fields.CharField')(max_length=192, null=True, db_index=True)),
            ('global_representation', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('account_homePage', self.gf('django.db.models.fields.CharField')(max_length=2083, blank=True)),
            ('account_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('lrs', ['Agent'])

        # Adding unique constraint on 'Agent', fields ['mbox', 'global_representation']
        db.create_unique('lrs_agent', ['mbox', 'global_representation'])

        # Adding unique constraint on 'Agent', fields ['mbox_sha1sum', 'global_representation']
        db.create_unique('lrs_agent', ['mbox_sha1sum', 'global_representation'])

        # Adding unique constraint on 'Agent', fields ['openID', 'global_representation']
        db.create_unique('lrs_agent', ['openID', 'global_representation'])

        # Adding unique constraint on 'Agent', fields ['oauth_identifier', 'global_representation']
        db.create_unique('lrs_agent', ['oauth_identifier', 'global_representation'])

        # Adding M2M table for field member on 'Agent'
        m2m_table_name = db.shorten_name('lrs_agent_member')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_agent', models.ForeignKey(orm['lrs.agent'], null=False)),
            ('to_agent', models.ForeignKey(orm['lrs.agent'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_agent_id', 'to_agent_id'])

        # Adding model 'AgentProfile'
        db.create_table('lrs_agentprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profileId', self.gf('django.db.models.fields.CharField')(max_length=2083, db_index=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('agent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lrs.Agent'])),
            ('profile', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
            ('json_profile', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content_type', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('etag', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
        ))
        db.send_create_signal('lrs', ['AgentProfile'])

        # Adding model 'Activity'
        db.create_table('lrs_activity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity_id', self.gf('django.db.models.fields.CharField')(max_length=2083, db_index=True)),
            ('objectType', self.gf('django.db.models.fields.CharField')(default='Activity', max_length=8, blank=True)),
            ('activity_definition_name', self.gf('jsonfield.fields.JSONField')(blank=True)),
            ('activity_definition_description', self.gf('jsonfield.fields.JSONField')(blank=True)),
            ('activity_definition_type', self.gf('django.db.models.fields.CharField')(max_length=2083, blank=True)),
            ('activity_definition_moreInfo', self.gf('django.db.models.fields.CharField')(max_length=2083, blank=True)),
            ('activity_definition_interactionType', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('activity_definition_extensions', self.gf('jsonfield.fields.JSONField')(blank=True)),
            ('activity_definition_crpanswers', self.gf('jsonfield.fields.JSONField')(blank=True)),
            ('activity_definition_choices', self.gf('jsonfield.fields.JSONField')(blank=True)),
            ('activity_definition_scales', self.gf('jsonfield.fields.JSONField')(blank=True)),
            ('activity_definition_sources', self.gf('jsonfield.fields.JSONField')(blank=True)),
            ('activity_definition_targets', self.gf('jsonfield.fields.JSONField')(blank=True)),
            ('activity_definition_steps', self.gf('jsonfield.fields.JSONField')(blank=True)),
            ('authoritative', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('global_representation', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('lrs', ['Activity'])

        # Adding unique constraint on 'Activity', fields ['activity_id', 'global_representation']
        db.create_unique('lrs_activity', ['activity_id', 'global_representation'])

        # Adding model 'StatementRef'
        db.create_table('lrs_statementref', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_type', self.gf('django.db.models.fields.CharField')(default='StatementRef', max_length=12)),
            ('ref_id', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('lrs', ['StatementRef'])

        # Adding model 'SubStatementContextActivity'
        db.create_table('lrs_substatementcontextactivity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('substatement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lrs.SubStatement'])),
        ))
        db.send_create_signal('lrs', ['SubStatementContextActivity'])

        # Adding M2M table for field context_activity on 'SubStatementContextActivity'
        m2m_table_name = db.shorten_name('lrs_substatementcontextactivity_context_activity')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('substatementcontextactivity', models.ForeignKey(orm['lrs.substatementcontextactivity'], null=False)),
            ('activity', models.ForeignKey(orm['lrs.activity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['substatementcontextactivity_id', 'activity_id'])

        # Adding model 'StatementContextActivity'
        db.create_table('lrs_statementcontextactivity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('statement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lrs.Statement'])),
        ))
        db.send_create_signal('lrs', ['StatementContextActivity'])

        # Adding M2M table for field context_activity on 'StatementContextActivity'
        m2m_table_name = db.shorten_name('lrs_statementcontextactivity_context_activity')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('statementcontextactivity', models.ForeignKey(orm['lrs.statementcontextactivity'], null=False)),
            ('activity', models.ForeignKey(orm['lrs.activity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['statementcontextactivity_id', 'activity_id'])

        # Adding model 'ActivityState'
        db.create_table('lrs_activitystate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state_id', self.gf('django.db.models.fields.CharField')(max_length=2083)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('state', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
            ('json_state', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('agent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lrs.Agent'])),
            ('activity_id', self.gf('django.db.models.fields.CharField')(max_length=2083, db_index=True)),
            ('registration_id', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('content_type', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('etag', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
        ))
        db.send_create_signal('lrs', ['ActivityState'])

        # Adding model 'ActivityProfile'
        db.create_table('lrs_activityprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profileId', self.gf('django.db.models.fields.CharField')(max_length=2083, db_index=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('activityId', self.gf('django.db.models.fields.CharField')(max_length=2083, db_index=True)),
            ('profile', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
            ('json_profile', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content_type', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('etag', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('lrs', ['ActivityProfile'])

        # Adding model 'SubStatement'
        db.create_table('lrs_substatement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_agent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='object_of_substatement', null=True, on_delete=models.SET_NULL, to=orm['lrs.Agent'])),
            ('object_activity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='object_of_substatement', null=True, on_delete=models.SET_NULL, to=orm['lrs.Activity'])),
            ('object_statementref', self.gf('django.db.models.fields.related.ForeignKey')(related_name='object_of_substatement', null=True, on_delete=models.SET_NULL, to=orm['lrs.StatementRef'])),
            ('actor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='actor_of_substatement', null=True, on_delete=models.SET_NULL, to=orm['lrs.Agent'])),
            ('verb', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lrs.Verb'], null=True, on_delete=models.SET_NULL)),
            ('result_success', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('result_completion', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('result_response', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('result_duration', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('result_score_scaled', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('result_score_raw', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('result_score_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('result_score_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('result_extensions', self.gf('jsonfield.fields.JSONField')(blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default='2013-10-24T04:01:15.216275+00:00', null=True, blank=True)),
            ('context_registration', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=40, blank=True)),
            ('context_instructor', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='substatement_context_instructor', null=True, on_delete=models.SET_NULL, to=orm['lrs.Agent'])),
            ('context_team', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='substatement_context_team', null=True, on_delete=models.SET_NULL, to=orm['lrs.Agent'])),
            ('context_revision', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('context_platform', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('context_language', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('context_extensions', self.gf('jsonfield.fields.JSONField')(blank=True)),
            ('context_statement', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
        ))
        db.send_create_signal('lrs', ['SubStatement'])

        # Adding model 'StatementAttachment'
        db.create_table('lrs_statementattachment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usageType', self.gf('django.db.models.fields.CharField')(max_length=2083)),
            ('contentType', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('length', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('sha2', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('fileUrl', self.gf('django.db.models.fields.CharField')(max_length=2083, blank=True)),
            ('payload', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
            ('display', self.gf('jsonfield.fields.JSONField')(blank=True)),
            ('description', self.gf('jsonfield.fields.JSONField')(blank=True)),
        ))
        db.send_create_signal('lrs', ['StatementAttachment'])

        # Adding model 'Group'
        db.create_table('lrs_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal('lrs', ['Group'])

        # Adding model 'Statement'
        db.create_table('lrs_statement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('statement_id', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=36, blank=True)),
            ('object_agent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='object_of_statement', null=True, on_delete=models.SET_NULL, to=orm['lrs.Agent'])),
            ('object_activity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='object_of_statement', null=True, on_delete=models.SET_NULL, to=orm['lrs.Activity'])),
            ('object_substatement', self.gf('django.db.models.fields.related.ForeignKey')(related_name='object_of_statement', null=True, on_delete=models.SET_NULL, to=orm['lrs.SubStatement'])),
            ('object_statementref', self.gf('django.db.models.fields.related.ForeignKey')(related_name='object_of_statement', null=True, on_delete=models.SET_NULL, to=orm['lrs.StatementRef'])),
            ('actor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='actor_statement', null=True, on_delete=models.SET_NULL, to=orm['lrs.Agent'])),
            ('verb', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lrs.Verb'], null=True, on_delete=models.SET_NULL)),
            ('result_success', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('result_completion', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('result_response', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('result_duration', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('result_score_scaled', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('result_score_raw', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('result_score_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('result_score_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('result_extensions', self.gf('jsonfield.fields.JSONField')(blank=True)),
            ('stored', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default='2013-10-24T04:01:15.224510+00:00', null=True, blank=True)),
            ('authority', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='authority_statement', null=True, on_delete=models.SET_NULL, to=orm['lrs.Agent'])),
            ('voided', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('context_registration', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=40, blank=True)),
            ('context_instructor', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='statement_context_instructor', null=True, on_delete=models.SET_NULL, to=orm['lrs.Agent'])),
            ('context_team', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='statement_context_team', null=True, on_delete=models.SET_NULL, to=orm['lrs.Agent'])),
            ('context_revision', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('context_platform', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('context_language', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('context_extensions', self.gf('jsonfield.fields.JSONField')(blank=True)),
            ('context_statement', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(default='1.0.0', max_length=7)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lrs.Group'], null=True, on_delete=models.SET_NULL)),
        ))
        db.send_create_signal('lrs', ['Statement'])

        # Adding M2M table for field attachments on 'Statement'
        m2m_table_name = db.shorten_name('lrs_statement_attachments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('statement', models.ForeignKey(orm['lrs.statement'], null=False)),
            ('statementattachment', models.ForeignKey(orm['lrs.statementattachment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['statement_id', 'statementattachment_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Activity', fields ['activity_id', 'global_representation']
        db.delete_unique('lrs_activity', ['activity_id', 'global_representation'])

        # Removing unique constraint on 'Agent', fields ['oauth_identifier', 'global_representation']
        db.delete_unique('lrs_agent', ['oauth_identifier', 'global_representation'])

        # Removing unique constraint on 'Agent', fields ['openID', 'global_representation']
        db.delete_unique('lrs_agent', ['openID', 'global_representation'])

        # Removing unique constraint on 'Agent', fields ['mbox_sha1sum', 'global_representation']
        db.delete_unique('lrs_agent', ['mbox_sha1sum', 'global_representation'])

        # Removing unique constraint on 'Agent', fields ['mbox', 'global_representation']
        db.delete_unique('lrs_agent', ['mbox', 'global_representation'])

        # Deleting model 'Nonce'
        db.delete_table('lrs_nonce')

        # Deleting model 'Consumer'
        db.delete_table('lrs_consumer')

        # Deleting model 'Token'
        db.delete_table('lrs_token')

        # Deleting model 'Verb'
        db.delete_table('lrs_verb')

        # Deleting model 'Agent'
        db.delete_table('lrs_agent')

        # Removing M2M table for field member on 'Agent'
        db.delete_table(db.shorten_name('lrs_agent_member'))

        # Deleting model 'AgentProfile'
        db.delete_table('lrs_agentprofile')

        # Deleting model 'Activity'
        db.delete_table('lrs_activity')

        # Deleting model 'StatementRef'
        db.delete_table('lrs_statementref')

        # Deleting model 'SubStatementContextActivity'
        db.delete_table('lrs_substatementcontextactivity')

        # Removing M2M table for field context_activity on 'SubStatementContextActivity'
        db.delete_table(db.shorten_name('lrs_substatementcontextactivity_context_activity'))

        # Deleting model 'StatementContextActivity'
        db.delete_table('lrs_statementcontextactivity')

        # Removing M2M table for field context_activity on 'StatementContextActivity'
        db.delete_table(db.shorten_name('lrs_statementcontextactivity_context_activity'))

        # Deleting model 'ActivityState'
        db.delete_table('lrs_activitystate')

        # Deleting model 'ActivityProfile'
        db.delete_table('lrs_activityprofile')

        # Deleting model 'SubStatement'
        db.delete_table('lrs_substatement')

        # Deleting model 'StatementAttachment'
        db.delete_table('lrs_statementattachment')

        # Deleting model 'Group'
        db.delete_table('lrs_group')

        # Deleting model 'Statement'
        db.delete_table('lrs_statement')

        # Removing M2M table for field attachments on 'Statement'
        db.delete_table(db.shorten_name('lrs_statement_attachments'))


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
            'secret': ('django.db.models.fields.CharField', [], {'default': "'xcPPMkS8pM'", 'max_length': '64'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'consumer_user'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'lrs.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
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
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lrs.Group']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
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
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': "'2013-10-24T04:01:15.280369+00:00'", 'null': 'True', 'blank': 'True'}),
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
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': "'2013-10-24T04:01:15.272330+00:00'", 'null': 'True', 'blank': 'True'}),
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
            'timestamp': ('django.db.models.fields.IntegerField', [], {'default': '1382587275L'}),
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