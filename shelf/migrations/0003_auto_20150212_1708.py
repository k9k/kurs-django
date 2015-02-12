# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20150210_1815'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'author', 'verbose_name_plural': 'authors', 'ordering': ('last_name', 'first_name')},
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(verbose_name='first_name', max_length=20),
            preserve_default=True,
        ),
    ]
