# Generated by Django 2.0.8 on 2018-09-17 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0007_auto_20180829_1733'),
        ('registers', '0008_auto_20180917_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='standardChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('expiry', models.DateField(blank=True, null=True)),
                ('approver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organisation.DepartmentUser')),
                ('it_system', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registers.ITSystem')),
            ],
        ),
        migrations.RemoveField(
            model_name='changerequest',
            name='change_duration',
        ),
        migrations.AddField(
            model_name='changerequest',
            name='change_end',
            field=models.DateTimeField(blank=True, help_text='Date change is planned to end.', null=True),
        ),
        migrations.AlterField(
            model_name='changerequest',
            name='change_start',
            field=models.DateTimeField(blank=True, help_text='Date change is planned to begin.', null=True),
        ),
    ]