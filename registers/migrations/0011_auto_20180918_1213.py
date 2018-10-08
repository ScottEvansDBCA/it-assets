# Generated by Django 2.0.8 on 2018-09-18 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0010_auto_20180917_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='changerequest',
            name='deployment_instructions',
        ),
        migrations.AddField(
            model_name='changerequest',
            name='broadcast',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='changerequest',
            name='implementation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='changerequest',
            name='implementation_docs',
            field=models.FileField(blank=True, null=True, upload_to='uploaded_files/'),
        ),
        migrations.AddField(
            model_name='changerequest',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='changerequest',
            name='outage',
            field=models.BooleanField(default=False),
        ),
    ]