# Generated by Django 2.1.4 on 2019-07-25 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datacatalog', '0017_auto_20190724_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='data_source',
            field=models.ForeignKey(blank=True, help_text='Group responsible for production of the data', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dataset_source', to='datacatalog.DataProvider'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='publication_date',
            field=models.DateField(blank=True, help_text='Publication date of the dataset', null=True),
        ),
        migrations.AlterField(
            model_name='datafield',
            name='scope',
            field=models.CharField(blank=True, help_text='Descriptions of the scope of the data (eg. min, max, number of records, number of null values, number of unique values)', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='access_requirements',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='datacatalog.DataAccess'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='data_fields',
            field=models.ManyToManyField(blank=True, help_text='List of all fields present in any schema', to='datacatalog.DataField'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='description',
            field=models.TextField(blank=True, help_text='Description of dataset, including purpose, scope, etc', null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='ds_id',
            field=models.CharField(blank=True, help_text='Unique identifer of the data set', max_length=128, null=True, unique=True, verbose_name='Dataset ID'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='expert',
            field=models.ForeignKey(blank=True, help_text='A local contact who is an expert on the data', null=True, on_delete=django.db.models.deletion.PROTECT, to='persons.Person'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='keywords',
            field=models.ManyToManyField(blank=True, help_text='Add keywords related to data set', to='datacatalog.Keyword'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='landing_url',
            field=models.URLField(blank=True, help_text='URL of page that allows access of data', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='media_subtype',
            field=models.ManyToManyField(blank=True, help_text='The media types of all files in data set', to='datacatalog.MediaSubType'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='period_end',
            field=models.DateField(blank=True, help_text='Date of latest data record', null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='period_start',
            field=models.DateField(blank=True, help_text='Date of earliest data record', null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='publisher',
            field=models.ForeignKey(help_text='Group responsible for publication of the data set', on_delete=django.db.models.deletion.PROTECT, related_name='dataset_publisher', to='datacatalog.DataProvider'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='title',
            field=models.CharField(help_text='The name of the dataset, usually one sentence or short description of the dataset', max_length=256, unique=True),
        ),
    ]