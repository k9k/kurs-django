# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_auto_20150215_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 16, 19, 19, 9, 915107, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
