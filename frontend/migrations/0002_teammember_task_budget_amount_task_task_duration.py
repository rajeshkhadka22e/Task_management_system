# Generated by Django 5.0 on 2024-10-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TeamMember",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("experience", models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name="task",
            name="budget_amount",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="task",
            name="task_duration",
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
