# Generated by Django 2.1.4 on 2019-02-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190201_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesmodel',
            name='soldto',
            field=models.CharField(default=True, max_length=30),
        ),
    ]