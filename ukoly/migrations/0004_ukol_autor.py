# Generated by Django 3.2.15 on 2022-09-06 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ukoly', '0003_ukol_jmeno_autora_alter_ukol_stav'),
    ]

    operations = [
        migrations.AddField(
            model_name='ukol',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ukoly_autora', to=settings.AUTH_USER_MODEL),
        ),
    ]
