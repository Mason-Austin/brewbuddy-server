# Generated by Django 4.1.3 on 2024-02-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewbuddyapi', '0002_brew_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='brew',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='brew_images/'),
        ),
    ]