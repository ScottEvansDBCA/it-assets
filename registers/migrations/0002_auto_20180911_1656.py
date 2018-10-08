# Generated by Django 2.0.8 on 2018-09-11 08:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0007_auto_20180829_1733'),
        ('registers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeApproval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(0, 'Open'), (1, 'Approved'), (2, 'Complete'), (3, 'Rejected')], default=0)),
                ('date_approved', models.DateField(help_text='Date change was approved/rejected.')),
                ('notes', models.CharField(blank=True, max_length=2048, null=True)),
                ('approver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organisation.DepartmentUser')),
            ],
        ),
        migrations.CreateModel(
            name='ChangeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=2048)),
                ('change_type', models.SmallIntegerField(choices=[(0, 'Normal'), (1, 'Standard'), (2, 'Emergency')], default=0)),
                ('urgency', models.SmallIntegerField(choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')], default=0)),
                ('submission_date', models.DateField(help_text='Date change was submitted.')),
                ('change_date', models.DateField(blank=True, help_text='Date change is planned for.', null=True)),
                ('change_duration', models.DurationField(default=datetime.timedelta(0, 3600), help_text='Amount of time change should take to perform (days hh:mm:ss).')),
                ('alternate_system', models.CharField(blank=True, max_length=255, null=True)),
                ('deployment_instructions', models.CharField(blank=True, max_length=2048, null=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Open'), (1, 'Approved'), (2, 'Complete'), (3, 'Rejected')], default=0)),
                ('unexpected_issues', models.BooleanField(default=False)),
                ('caused_issues', models.BooleanField(default=False)),
                ('approver', models.ForeignKey(help_text='System owner', on_delete=django.db.models.deletion.PROTECT, related_name='system_owner', to='organisation.DepartmentUser')),
                ('implementer', models.ForeignKey(help_text='Request carried out by', on_delete=django.db.models.deletion.PROTECT, related_name='request_providor', to='organisation.DepartmentUser')),
                ('it_system', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registers.ITSystem')),
                ('requestor', models.ForeignKey(help_text='Request owner', on_delete=django.db.models.deletion.PROTECT, related_name='request_creator', to='organisation.DepartmentUser')),
            ],
        ),
        migrations.AddField(
            model_name='changeapproval',
            name='change_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registers.ChangeRequest'),
        ),
    ]