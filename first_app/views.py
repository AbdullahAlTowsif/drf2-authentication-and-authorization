from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from . import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AdminOrReadOnly]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    
    # search filtering
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'description']
    
    # order filtering
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['price']


class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.ReviewerOrReadOnly]
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializer
    
    # filter
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['user__username']
    # filterset_fields = ['rating', 'product']
    
    # ordering filter
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating']
    
    # when we use filter_backends, filterset_fields follow below steps:
    # 1. api will be: http://127.0.0.1:8000/reviews/?user__username=towsif
    # http://127.0.0.1:8000/reviews/?rating=3, http://127.0.0.1:8000/reviews/?rating=3&product=2
    # 2. use: queryset = models.ProductReview.objects.all()
    
    # def get_queryset(self):
    #     queryset = models.ProductReview.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         # icontains means not case-sensitive
    #         queryset = queryset.filter(user__username__icontains=username)
    #     return queryset
    
    # when we use this queryset function for filter follow below steps:
    # 1. api will be: http://127.0.0.1:8000/reviews/?username=towsif
    # 2. don't use: queryset = models.ProductReview.objects.all()
