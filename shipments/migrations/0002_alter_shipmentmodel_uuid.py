# Generated by Django 4.0.6 on 2022-07-22 07:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipmentmodel',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
