from rest_framework import serializers

class CitydayValidator(serializers.Serializer):
    city1 = serializers.CharField(required=True)
    day = serializers.IntegerField(required=True)

    #Validating the given day
    def validate_day(self,value):
        if value > 7 or value < 1:
            raise serializers.ValidationError(f"L'utilisateur n'existe pas.")

        return value - 1
