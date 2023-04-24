# Generated by Django 4.1.3 on 2023-01-06 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0005_remove_bookinstance_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='user_loved',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
