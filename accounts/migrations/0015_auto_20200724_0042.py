# Generated by Django 3.0.7 on 2020-07-24 04:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20200724_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxlist',
            name='associated_customer',
            field=models.EmailField(blank=True, default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='boxlist',
            name='filledTime',
            field=models.DateTimeField(blank=True),
        ),
    ]