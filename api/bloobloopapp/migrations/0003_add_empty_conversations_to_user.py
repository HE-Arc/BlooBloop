# Generated by Django 4.1.5 on 2023-03-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bloobloopapp", "0002_create_profile_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profileitem",
            name="conversations",
            field=models.ManyToManyField(
                blank=True, to="bloobloopapp.conversationitem"
            ),
        ),
    ]
