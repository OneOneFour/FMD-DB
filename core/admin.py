from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Country)
admin.site.register(Batch)
admin.site.register(Host)
admin.site.register(TaxonomicCategory)
admin.site.register(TaxonomicGroup)
admin.site.register(NucleotideSequence)
admin.site.register(VirusGenome)
admin.site.register(VirusSample)
