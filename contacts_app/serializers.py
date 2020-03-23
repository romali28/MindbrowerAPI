from rest_framework import serializers
from contacts_app.models import Contacts


# class ContactsSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(
#         required=True, allow_blank=False, max_length=100)
#     number = serializers.CharField(
#         required=True, allow_blank=True, max_length=100)
#     photo = serializers.CharField(
#         required=False, allow_blank=False, max_length=100)
#     favorite = serializers.BooleanField(required=True)
#     deleted = serializers.BooleanField(required=True)


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'name', 'number', 'photo', 'favorite', 'deleted']
