# Generated by Django 4.2.6 on 2023-10-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_buku_gambar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='gambar',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
