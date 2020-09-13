# Generated by Django 3.1.1 on 2020-09-12 02:46

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import meeting.models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingCreate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('due_date', models.DateTimeField()),
                ('invite_url', models.URLField()),
                ('member_list', jsonfield.fields.JSONField(null=True)),
                ('isOnlyDate', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='MeetingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matched_date', models.DateField()),
                ('matched_time', models.TimeField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_time', to='meeting.meetingcreate')),
            ],
            options={
                'ordering': ['team'],
                'unique_together': {('team', 'matched_date', 'matched_time')},
            },
        ),
        migrations.DeleteModel(
            name='MeetingResult',
        ),
        migrations.AlterModelOptions(
            name='meetinginput',
            options={'ordering': ['team']},
        ),
        migrations.AddField(
            model_name='meetinginput',
            name='date',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='meetinginput',
            name='timetable',
            field=jsonfield.fields.JSONField(default=meeting.models.timetable_default),
        ),
        migrations.AddField(
            model_name='meetinginput',
            name='team',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='team_input', to='meeting.meetingcreate'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='meetinginput',
            unique_together={('team', 'date', 'dummyname', 'timetable')},
        ),
    ]
