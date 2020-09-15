# Generated by Django 3.1 on 2020-08-27 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0006_auto_20200827_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetinginput',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_input', to='meeting.meetingcreate'),
        ),
        migrations.AlterField(
            model_name='meetingtime',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_time', to='meeting.meetingcreate'),
        ),
    ]