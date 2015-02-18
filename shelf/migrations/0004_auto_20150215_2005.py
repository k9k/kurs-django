# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0003_auto_20150212_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedition',
            name='book',
            field=models.ForeignKey(to='shelf.Book', related_name='editions'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookedition',
            name='isbn',
            field=models.CharField(max_length=17, blank=True),
            preserve_default=True,
        ),
    ]
