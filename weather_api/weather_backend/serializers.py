from rest_framework import serializers

class CitydayValidator(serializers.Serializer):
    city1 = serializers.CharField(default=True)
    first_choice_day = serializers.IntegerField(default=True, max_value=7, min_value=0)

