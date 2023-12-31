# Generated by Django 4.2.6 on 2023-10-25 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_buku_jumlah_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='bahasa',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='buku',
            name='judul',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='buku',
            name='jumlah_halaman',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='buku',
            name='jumlah_review',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='buku',
            name='penerbit',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='buku',
            name='penulis',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
