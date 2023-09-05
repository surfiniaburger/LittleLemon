from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu  # Import the Menu model from your app
from restaurant.serializers import MenuSerializer  # Import the MenuSerializer from your app

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a few test instances of the Menu model
        Menu.objects.create(title="Burger", price=10.99)
        Menu.objects.create(title="Pizza", price=12.99)
        Menu.objects.create(title="Salad", price=8.49)

        # Create an instance of the APIClient
        self.client = APIClient()

    def test_getall(self):
        # Define the URL for the MenuItemsView using reverse
        url = '/menu/'  # Replace with the actual URL for your view

        # Perform a GET request to retrieve all Menu objects
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Retrieve all Menu objects from the database
        menu_items = Menu.objects.all()

        # Serialize the retrieved objects
        serializer = MenuSerializer(menu_items, many=True)

        # Check if the serialized data in the response matches the expected data
        self.assertEqual(response.data, serializer.data)
