from rest_framework import viewsets
from .serializers import *


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer


class TaxonomicCategoryViewSet(viewsets.ModelViewSet):
    queryset = TaxonomicCategory.objects.all()
    serializer_class = TaxonomicCategorySerializer


class TaxonomicGroupViewSet(viewsets.ModelViewSet):
    queryset = TaxonomicGroup.objects.all()
    serializer_class = TaxonomicGroupSerializer


class NucleotideSequenceViewSet(viewsets.ModelViewSet):
    queryset = NucleotideSequence.objects.all()
    serializer_class = NucleotideSequenceSerializer


class VirusSampleViewSet(viewsets.ModelViewSet):
    queryset = VirusSample.objects.all()
    serializer_class = VirusSampleSerializer


class VirusGenomeViewSet(viewsets.ModelViewSet):
    queryset = VirusGenome.objects.all()
    serializer_class = VirusGenomeSerializer
