# Generated by Django 4.1 on 2022-12-20 10:12

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_category_main_category_sub_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_quantity', models.IntegerField()),
                ('Availability', models.IntegerField()),
                ('featured_image', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('Discount', models.IntegerField()),
                ('Product_information', ckeditor.fields.RichTextField()),
                ('model_Name', models.CharField(max_length=100)),
                ('Tags', models.CharField(max_length=100)),
                ('Description', ckeditor.fields.RichTextField()),
                ('Categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_url', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Store.section'),
        ),
        migrations.CreateModel(
            name='Additional_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.product')),
            ],
        ),
    ]
