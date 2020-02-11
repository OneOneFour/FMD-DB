from rest_framework import serializers
from .models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'


class TaxonomicCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxonomicCategory
        fields = '__all__'


class TaxonomicGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxonomicGroup
        fields = '__all__'


class NucleotideSequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NucleotideSequence
        fields = '__all__'


class VirusSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirusSample
        fields = '__all__'


class VirusGenomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirusGenome
        fields = '__all__'
