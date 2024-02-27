from rest_framework import serializers
from .models import BlogPost, Car

class CitydayValidator(serializers.Serializer):
    city = serializers.CharField(required=True)
    day = serializers.IntegerField(required=True)

    #Validating the given day
    def validate_day(self,value):
        if value > 7 or value < 1:
            raise serializers.ValidationError(f"Error in the choosed day!")

        return value - 1


# Serializer for the Blog model
class BlogPostVAlidator(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'category']


# serializing Car model
class CarSerializer(serializers.ModelSerializer):
    insured = serializers.BooleanField()
    class Meta:
        model = Car
        fields = ['pk', 'name', 'color', 'price', 'insured', 'type']


