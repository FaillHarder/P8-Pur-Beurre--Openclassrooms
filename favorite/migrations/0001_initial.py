# Generated by Django 3.2.4 on 2021-08-28 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_favorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.product')),
            ],
        ),
    ]
