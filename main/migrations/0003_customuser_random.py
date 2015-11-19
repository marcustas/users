# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customuser_bdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='random',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
