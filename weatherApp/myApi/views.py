from django.shortcuts import render
from django.http import HttpResponse

# basic setup for the API
from myApi.models import Plan
from myApi.serializers import PlanSerializer

# rest_framework basic setup
from rest_framework import status

# class based view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView

# generic  based view
from rest_framework import mixins
from rest_framework import generics
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

# Create your views here.

class PlanList(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    
class PlanCreate(CreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PlanDestroy(DestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    lookup_field = 'id'