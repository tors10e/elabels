# Generated by Django 2.0 on 2020-02-20 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elabels', '0006_applicationrate_application_method'),
    ]

    operations = [
        migrations.RenameField(
            model_name='label',
            old_name='name',
            new_name='product_name',
        ),
    ]
