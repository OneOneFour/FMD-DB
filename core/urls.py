from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'batches', views.BatchViewSet)
router.register(r'hosts', views.HostViewSet)
router.register(r'taxonomic_cateogories', views.TaxonomicCategoryViewSet)
router.register(r'taxonomic_groups', views.TaxonomicGroupViewSet)
router.register(r'nucleotide_sequences', views.NucleotideSequenceViewSet)
router.register(r'virus_genomes', views.VirusGenomeViewSet)
router.register(r'virus_samples', views.VirusSampleViewSet)

urlpatterns = [
    path('', include(router.urls))
]
