# Generated by Django 3.1.6 on 2021-02-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("visitors", "0004_visitor_expires_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="visitorlog",
            name="status_code",
            field=models.PositiveIntegerField(default=0, verbose_name="HTTP Response"),
        ),
    ]
