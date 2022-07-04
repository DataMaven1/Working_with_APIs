from rest_framework import generic
from django.shortcuts import render
from links.models import Link

from links.serializers import LinkSerializer

# Create your views here.
class PostListApi(generic.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostCreateApi(generic.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDetailApi(generic.RetreiveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostUpdateApi(generic.UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDeleteApi(generic.DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer