# Generated by Django 4.1.5 on 2023-08-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_material_alter_customer_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='wikipedia_url',
            field=models.URLField(blank=True),
        ),
    ]