# Generated by Django 3.1.7 on 2021-04-02 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_product_sub_saved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['nutriscore_grade']},
        ),
        migrations.AlterModelOptions(
            name='sub_saved',
            options={},
        ),
    ]
