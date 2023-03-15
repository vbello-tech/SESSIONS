# Generated by Django 4.1.7 on 2023-03-15 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, upload_to='Business/')),
                ('description', models.CharField(blank=True, max_length=60, null=True)),
                ('category', models.CharField(max_length=200)),
                ('active', models.BooleanField(default='True')),
                ('sessions_completed', models.IntegerField(blank=True, default=0, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('banned_date', models.DateTimeField(blank=True, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('code', models.SlugField(blank=True, null=True, unique=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Business',
                'ordering': ['-created_date'],
            },
        ),
    ]
