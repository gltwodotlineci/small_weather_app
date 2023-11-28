from rest_framework import serializers

class CitydayValidator(serializers.Serializer):
    city = serializers.CharField(required=True)
    day = serializers.IntegerField(required=True)

    #Validating the given day
    def validate_day(self,value):
        if value > 7 or value < 1:
            raise serializers.ValidationError(f"Error in the choosed day!")

        return value - 1
