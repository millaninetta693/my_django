from rest_framework import generics, mixins, permissions
from ..models import Reference
from .serializers import ReferenceSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework.response import Response 
from django.contrib.auth import get_user_model 
from .permissions import IsAuthorOrReadonly
from django.utils.text import slugify

# class PostListView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class ReferenceListView(generics.ListCreateAPIView):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if serializer.is_valid():
         serializer.save(author=self.request.user,
                         slug=slugify(serializer.validated_data['title'], allow_unicode=True))
                         
class ReferenceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadonly]

    def perform_update(self, serializer):
        if serializer.is_valid():
         serializer.save(slug=slugify(serializer.validated_data['title'], allow_unicode=True))
    # def get(self, request, *args, **kwargs):
