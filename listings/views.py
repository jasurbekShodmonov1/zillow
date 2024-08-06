from rest_framework import viewsets
from .models import Property, Listing
from .serializers import PropertySerializer, ListingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    @action(detail=False, methods=['get'], url_path='buy')
    def buy(self, request):
        listings = self.get_queryset().filter(transaction_type='buy', is_published=True)
        serializer = self.get_serializer(listings, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='rent')
    def rent(self, request):
        listings = self.get_queryset().filter(transaction_type='rent', is_published=True)
        serializer = self.get_serializer(listings, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='sell')
    def sell(self, request):
        listings = self.get_queryset().filter(transaction_type='sell', is_published=True)
        serializer = self.get_serializer(listings, many=True)
        return Response(serializer.data)

    # @action(detail=False, methods=['get'], url_path='find')
    # # def find(self, request):
    # #     city = request.query_params.get('city', None)
    # #     state = request.query_params.get('state', None)
    # #     listings = self.get_queryset().filter(is_published=True)
    # #     if city:
    # #         listings = listings.filter(property__city__icontains=city)
    # #     if state:
    # #         listings = listings.filter(property__state__icontains(state))
    # #     serializer = self.get_serializer(listings, many=True)
    # #     return Response(serializer.data)


