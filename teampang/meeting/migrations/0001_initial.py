# Generated by Django 3.1 on 2020-11-19 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date_range', jsonfield.fields.JSONField(null=True)),
                ('confirmed_date', models.DateTimeField(null=True)),
                ('invite_url', models.URLField()),
                ('member_list', jsonfield.fields.JSONField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DummyPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', jsonfield.fields.JSONField(null=True)),
                ('connected_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DummyPlan', to='meeting.plan')),
            ],
        ),
    ]
