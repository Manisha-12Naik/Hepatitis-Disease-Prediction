# Generated by Django 5.0.4 on 2024-05-28 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heptities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.IntegerField()),
                ('Age', models.IntegerField()),
                ('Sex', models.CharField(max_length=500)),
                ('ALB', models.IntegerField()),
                ('ALP', models.IntegerField()),
                ('ALT', models.IntegerField()),
                ('AST', models.IntegerField()),
                ('BIL', models.IntegerField()),
                ('CHE', models.IntegerField()),
                ('CHOL', models.IntegerField()),
                ('CREA', models.IntegerField()),
                ('GGT', models.IntegerField()),
                ('PROT', models.IntegerField()),
            ],
        ),
    ]
