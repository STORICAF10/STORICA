# Generated by Django 4.2.5 on 2023-10-27 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_remove_buku_id_buku_buku_isi_buku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buku',
            name='isi_buku',
        ),
        migrations.RemoveField(
            model_name='buku',
            name='user',
        ),
        migrations.AlterField(
            model_name='buku',
            name='bahasa',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='buku',
            name='gambar',
            field=models.ImageField(blank=True, default='default_cover.png', null=True, upload_to=''),
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
        migrations.AlterField(
            model_name='buku',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='buku',
            name='tanggal_terbit',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kata_kata', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField()),
                ('buku_total', models.PositiveIntegerField()),
                ('batas_atas', models.PositiveIntegerField()),
                ('persen', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BukuKreasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(blank=True, max_length=255, null=True)),
                ('jumlah_halaman', models.PositiveIntegerField(blank=True, null=True)),
                ('bahasa', models.CharField(blank=True, max_length=50, null=True)),
                ('penulis', models.CharField(blank=True, max_length=255, null=True)),
                ('penerbit', models.CharField(blank=True, max_length=255, null=True)),
                ('jumlah_review', models.PositiveIntegerField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('gambar', models.ImageField(blank=True, default='default_cover.png', null=True, upload_to='')),
                ('tanggal_terbit', models.DateField(blank=True, null=True)),
                ('is_published', models.BooleanField()),
                ('isi_buku', models.TextField(blank='', null='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
