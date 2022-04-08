from rest_framework import serializers

from first_app.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_rate(self, value):
        if value < 0:
            raise serializers.ValidationError('Positive values only!')
        return value
