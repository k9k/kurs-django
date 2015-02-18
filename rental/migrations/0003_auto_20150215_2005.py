# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_auto_20150212_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 15, 20, 5, 8, 860311, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
