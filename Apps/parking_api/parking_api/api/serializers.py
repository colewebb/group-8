from rest_framework import serializers

from account.models import Account

class RegistrationSerializer(serializers.ModelSerializer):

    confirmPassword = serializers.CharField(style-{'input_type': 'password'}, whrite_only=True)

    class Meta:
        model = Acocunt
        fields = ['email', 'username', 'password', 'confirmPassword']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
                email=self.validated_data['email'],
                username=self.validated_data['username'],
            )
        password = self.validated_data['password']
        confirmPassword = self.validated_data['confirmPassword']

        if password != confirmPassword:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account
