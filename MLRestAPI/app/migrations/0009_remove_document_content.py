# Generated by Django 4.1.5 on 2023-02-09 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_sentence_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='content',
        ),
    ]
