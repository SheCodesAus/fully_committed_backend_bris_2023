# Generated by Django 4.2.6 on 2023-10-08 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('her_profiles', '0002_alter_herprofile_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=200, null=True)),
                ('skill_slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='herprofile',
            name='skills',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='her_profiles.skills'),
        ),
    ]
