# Generated by Django 4.1.3 on 2024-02-17 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('uid', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=500)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BrewLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.TextField()),
                ('date', models.DateField()),
                ('brew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbuddyapi.brew')),
            ],
        ),
        migrations.CreateModel(
            name='BrewCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='brewbuddyapi.brew')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brews', to='brewbuddyapi.category')),
            ],
        ),
        migrations.AddField(
            model_name='brew',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewbuddyapi.user'),
        ),
    ]
