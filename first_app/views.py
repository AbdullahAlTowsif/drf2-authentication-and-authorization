from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from . import permissions

class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AdminOrReadOnly]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.ReviewerOrReadOnly]
    # queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializer
    def get_queryset(self):
        queryset = models.ProductReview.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            # icontains means not case-sensitive
            queryset = queryset.filter(user__username__icontains=username)
        return queryset