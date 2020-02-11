from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    alpha_3_code = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Countries"


class Batch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Batches"


class Host(models.Model):
    name = models.CharField(max_length=100)
    taxonomy_id = models.IntegerField()
    description = models.TextField()


class TaxonomicCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Taxonomic Categories"


class TaxonomicGroup(models.Model):
    taxonomic_category = models.ForeignKey(TaxonomicCategory, on_delete=models.CASCADE)  # need more specification here
    supergroup = models.TextField()
    name = models.CharField(max_length=100)


class VirusSample(models.Model):
    name = models.CharField(max_length=100)
    wrl_ref_no = models.CharField(max_length=20)
    description = models.TextField()
    location = models.CharField(max_length=100)
    collection_date_range = models.DateField()
    reception_date_range = models.DateField()
    sender_reference = models.CharField(max_length=100)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    laboratory = models.TextField(max_length=100)


class VirusGenome(models.Model):
    name = models.CharField(max_length=100)
    virus_sample = models.ForeignKey(VirusSample, on_delete=models.CASCADE)
    taxonomic_group = models.ForeignKey(TaxonomicGroup, on_delete=models.CASCADE)
    description = models.TextField()


class NucleotideSequence(models.Model):
    PUBLIC = 0
    PRIVATE = 1
    CONFIDENTIAL = 2
    SECURITY_CHOICES = ((PUBLIC, "Public"), (PRIVATE, "Private"), (CONFIDENTIAL, "Confidential"))

    name = models.CharField(max_length=20)
    gen_bank_accession = models.CharField(max_length=50)
    virus_genome = models.ForeignKey(VirusGenome, on_delete=models.CASCADE)
    byte_sequence = models.TextField()
    description = models.TextField()
    creation_date = models.DateField()
    laboratory = models.CharField(max_length=50)
    laboratory_staff = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    material_harvest_date = models.DateField()
    primers = models.CharField(max_length=100)
    reception_date = models.DateField()
    security = models.IntegerField(choices=SECURITY_CHOICES)
