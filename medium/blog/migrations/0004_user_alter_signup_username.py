# Generated by Django 4.1.2 on 2022-11-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_login"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("username", models.CharField(max_length=10)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
            options={"db_table": "user",},
        ),
        migrations.AlterField(
            model_name="signup", name="username", field=models.CharField(max_length=10),
        ),
    ]
