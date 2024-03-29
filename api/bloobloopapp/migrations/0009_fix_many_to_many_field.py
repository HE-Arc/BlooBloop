# Generated by Django 4.1.5 on 2023-03-29 13:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bloobloopapp", "0008_remove_null_conversation_to_message"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profileitem",
            name="conversations",
        ),
        migrations.AlterField(
            model_name="conversationitem",
            name="users",
            field=models.ManyToManyField(
                related_name="conversation_items", to="bloobloopapp.profileitem"
            ),
        ),
    ]
