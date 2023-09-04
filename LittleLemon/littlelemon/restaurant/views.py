from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import viewsets, permissions


# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def home_view(request):
    # Your view logic here...
    return render(request, 'home.html', {})


class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()  # Define your queryset
    serializer_class = MenuSerializer  # Replace with your serializer class for Menu

    # You can override any other methods or attributes as needed for handling POST and GET requests.

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()  # Define your queryset
    serializer_class = MenuSerializer  # Replace with your serializer class for Menu

    # You can override any other methods or attributes as needed for handling GET, PUT, and DELETE requests.

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Fetch all objects from the Booking model
    serializer_class = BookingSerializer  # Set the serializer class to BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    # standard CRUD (Create, Retrieve, Update, Delete) operations 