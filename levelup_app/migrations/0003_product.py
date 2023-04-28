# Generated by Django 4.1.6 on 2023-04-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelup_app', '0002_alter_userimage_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]