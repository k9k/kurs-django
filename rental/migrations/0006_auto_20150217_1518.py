# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_auto_20150216_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 17, 15, 18, 39, 658021, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
