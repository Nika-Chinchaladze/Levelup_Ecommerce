# Generated by Django 4.1.6 on 2023-04-28 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('levelup_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_image', to=settings.AUTH_USER_MODEL),
        ),
    ]