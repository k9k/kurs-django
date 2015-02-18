# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 12, 18, 26, 32, 947922, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
