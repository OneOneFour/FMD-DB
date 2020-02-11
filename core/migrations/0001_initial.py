# Generated by Django 3.0.3 on 2020-02-08 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Batches',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alpha_3_code', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('taxonomy_id', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TaxonomicCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Taxonomic Categories',
            },
        ),
        migrations.CreateModel(
            name='TaxonomicGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supergroup', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('taxonomic_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TaxonomicCategory')),
            ],
        ),
        migrations.CreateModel(
            name='VirusSample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('wrl_ref_no', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('collection_date_range', models.DateField()),
                ('reception_date_range', models.DateField()),
                ('sender_reference', models.CharField(max_length=100)),
                ('laboratory', models.TextField(max_length=100)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Batch')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Country')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Host')),
            ],
        ),
        migrations.CreateModel(
            name='VirusGenome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('taxonomic_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TaxonomicGroup')),
                ('virus_sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.VirusSample')),
            ],
        ),
        migrations.CreateModel(
            name='NucleotideSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gen_bank_accession', models.CharField(max_length=50)),
                ('byte_sequence', models.TextField()),
                ('description', models.TextField()),
                ('creation_date', models.DateField()),
                ('laboratory', models.CharField(max_length=50)),
                ('laboratory_staff', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('material_harvest_date', models.DateField()),
                ('primers', models.CharField(max_length=100)),
                ('reception_date', models.DateField()),
                ('security', models.IntegerField(choices=[(0, 'Public'), (1, 'Private'), (2, 'Confidential')])),
                ('virus_genome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.VirusGenome')),
            ],
        ),
    ]
