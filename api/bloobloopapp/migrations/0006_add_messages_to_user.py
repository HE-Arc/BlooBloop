# Generated by Django 4.1.5 on 2023-03-02 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("bloobloopapp", "0005_sorcellerie_many_to_many"),
    ]

    operations = [
        migrations.AddField(
            model_name="messageitem",
            name="profile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="message_items",
                to="bloobloopapp.profileitem",
            ),
        ),
    ]
