# Generated by Django 3.1 on 2020-08-27 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0005_remove_meetingtime_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meetinginput',
            options={'ordering': ['team']},
        ),
        migrations.AlterModelOptions(
            name='meetingtime',
            options={'ordering': ['team']},
        ),
        migrations.AddField(
            model_name='meetingtime',
            name='team',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='meeting.meetingcreate'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='meetinginput',
            unique_together={('team', 'dummyname', 'timetable')},
        ),
        migrations.AlterUniqueTogether(
            name='meetingtime',
            unique_together={('team', 'matched_date', 'matched_time')},
        ),
    ]