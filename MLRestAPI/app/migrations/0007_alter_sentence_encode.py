# Generated by Django 4.1.5 on 2023-02-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_sentence_encode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='encode',
            field=models.BinaryField(editable=True),
        ),
    ]
