# Generated by Django 5.2.3 on 2025-06-28 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttracker',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='producttracker',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trackers', to='app.product'),
        ),
        migrations.AddField(
            model_name='producttracker',
            name='tracking_id',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True, unique=True),
        ),
    ]
