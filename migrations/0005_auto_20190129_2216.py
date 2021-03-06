# Generated by Django 2.1.4 on 2019-01-30 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datacatalog', '0004_auto_20190124_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='datauseagreement',
            name='reuse_scope',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datauseagreement',
            name='access_requirements',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacatalog.DataAccess'),
        ),
    ]
