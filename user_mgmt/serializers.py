# accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser, UserProfile
from datetime import date


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['date_of_birth', 'address', 'phone_number', 'profile_photo']

    def validate_date_of_birth(self, value):
        # Ensure date_of_birth does not exceed current date
        if value and value > date.today():  # Check if value is provided
            raise serializers.ValidationError("Date of birth cannot be in the future.")

        # Calculate age only if date_of_birth is provided
        if value:
            age = date.today().year - value.year - ((date.today().month, date.today().day) < (value.month, value.day))

            # Ensure user is at least 12 years old
            if age < 12:
                raise serializers.ValidationError("User must be at least 12 years old.")

        return value
