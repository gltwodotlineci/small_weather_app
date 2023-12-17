from rest_framework import serializers
from .models import Customuser


class SignUpValidator(serializers.Serializer):
    name = serializers.Charfield(required=True)
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)
    passowrd = password2

    def validate_password1(self, value):
        if value == self.passowrd:
            return True
        raise serializers.ValidationError(f"Erreur de saisie les mot de passes doivent être identiques")
