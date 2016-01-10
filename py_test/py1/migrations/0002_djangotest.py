# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('py1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='djangotest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dname', models.CharField(max_length=200)),
                ('dage', models.IntegerField(default=0)),
            ],
        ),
    ]
