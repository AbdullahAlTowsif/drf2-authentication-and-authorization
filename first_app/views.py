from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializer