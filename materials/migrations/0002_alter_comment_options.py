# Generated by Django 5.2 on 2025-05-14 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_at',), 'verbose_name': 'comment', 'verbose_name_plural': 'comments'},
        ),
    ]
