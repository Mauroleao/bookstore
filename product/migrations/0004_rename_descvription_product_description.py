# Generated by Django 5.1.5 on 2025-01-28 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descvription',
            new_name='description',
        ),
    ]
