from rest_framework import generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import *
from rest_framework.permissions import *

# Create your views here.

#generate random 5 digits that would be used as business code.
def code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

class BusinessCreateViewSet(viewsets.ModelViewSet):

    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user, code=code())
        return super().perform_create(serializer)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getbusiness(request, pk):
    """returns business with pk==pk """
    business = Business.objects.get(pk=pk)
    serializer = BusinessSerializer(business, many=False)
    if serializer:
        return Response({
            'name': business.name,
            'active': business.active,
            'id': business.id,
        })


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getcategory(request, category):
    """returns all registered businesses with category==category"""
    business = Business.objects.filter(category=category)
    serializer = BusinessSerializer(business, many=True)
    if serializer:
        return Response({
            'message': f'BUSINESSES UNDER {category}',
            'business': serializer.data
        })


