# Generated by Django 4.2.5 on 2023-12-30 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('FaTitle', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=1000)),
                ('FaText', models.CharField(max_length=1000)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=1000)),
                ('Email', models.EmailField(max_length=254)),
                ('Comment', models.CharField(max_length=20000)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('FaTitle', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=1000)),
                ('FaText', models.CharField(max_length=1000)),
                ('main_image', models.ImageField(upload_to='uploadedimages/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('FaName', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2000)),
                ('FaDescription', models.TextField(max_length=2000)),
                ('image', models.ImageField(upload_to='uploadedimages/')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Faname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='uploadedimages/')),
                ('pro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.type'),
        ),
    ]
