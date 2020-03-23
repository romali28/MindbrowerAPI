from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

# import models
from contacts_app.models import Contacts

#import Serializer
from contacts_app.serializers import ContactsSerializer

# Create your views here.
@api_view(['GET'])
def get_contacts(req):

    contacts = Contacts.objects.all()
    serializer = ContactsSerializer(contacts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_favorite(req):
    req_body = json.loads(req.body)
    id = req_body['id']
    Contacts.objects.filter(id=id).update(favorite=True)
    contacts = Contacts.objects.all()
    serializer = ContactsSerializer(contacts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def remove_favorite(req):

    req_body = json.loads(req.body)
    id = req_body['id']
    Contacts.objects.filter(id=id).update(favorite=False)
    contacts = Contacts.objects.all()
    serializer = ContactsSerializer(contacts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def delete_contact(req):

    req_body = json.loads(req.body)
    id = req_body['id']
    Contacts.objects.filter(id=id).update(deleted=True)
    contacts = Contacts.objects.all()
    serializer = ContactsSerializer(contacts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def restore_contact(req):
    req_body = json.loads(req.body)
    id = req_body['id']
    Contacts.objects.filter(id=id).update(deleted=False)
    contacts = Contacts.objects.all()
    serializer = ContactsSerializer(contacts, many=True)
    return Response(serializer.data)
