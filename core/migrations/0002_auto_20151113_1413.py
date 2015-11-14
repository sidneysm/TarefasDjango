# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='prazo',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 13, 17, 13, 36, 343189, tzinfo=utc)),
        ),
    ]
