# Generated by Django 4.1.3 on 2023-12-17 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_buku_isi_buku_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buku',
            name='isi_buku',
        ),
    ]
