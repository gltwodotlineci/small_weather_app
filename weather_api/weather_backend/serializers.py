from rest_framework import serializers

class CitydayValidator(serializers.Serializer):
    city1 = serializers.CharField(required=True)
    day = serializers.IntegerField(required=True)

    #Validating the given day
    def validate_day(self,value):
        if value > 7 or value < 1:
            raise serializers.ValidationError(f"Error in the choosed day!")

        return value - 1


# Validation of the second city
class SecondCityValidator(serializers.Serializer):
    city2=serializers.CharField(required=False)
    day2=serializers.IntegerField(required=False)

    #Validate the given day 2
    def validate_day2(self,value):
        if value > 7 or value < 1:
            raise serializers.ValidationError(f"Error in the choosed day!")

        return value -1
