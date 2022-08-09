from rest_framework import serializers
from .models import *






class CovidSerializer(serializers.ModelSerializer):
    #upload_documents = serializers.FileField(max_length=None, use_url=True)
    class  Meta:
          model        =           Covidcases
          fields       =           '__all__'
