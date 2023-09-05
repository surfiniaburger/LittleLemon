# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from restaurant.models import Menu  # Import the Menu model from your app
# from restaurant.serializers import MenuSerializer  # Import the MenuSerializer from your app

# class MenuViewTest(TestCase):
#     def setUp(self):
#         # Create a few test instances of the Menu model
#         Menu.objects.create(title="Burger", price=10.99)
#         Menu.objects.create(title="Pizza", price=12.99)
#         Menu.objects.create(title="Salad", price=8.49)

#         # Create an instance of the APIClient
#         self.client = APIClient()

#     def test_getall(self):
#         # Define the URL for the MenuItemsView using reverse
#         url = '/menu/'  # Replace with the actual URL for your view

#         # Perform a GET request to retrieve all Menu objects
#         response = self.client.get(url)

#         # Check if the response status code is 200 (OK)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         # Retrieve all Menu objects from the database
#         menu_items = Menu.objects.all()

#         # Serialize the retrieved objects
#         serializer = MenuSerializer(menu_items, many=True)

#         # Check if the serialized data in the response matches the expected data
#         self.assertEqual(response.data, serializer.data)

# from django.test import TestCase
# from restaurant.models import Menu
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# import json

# class MenuViewTest(TestCase):
#     def setUp(self):
#         # Create a few test instances of the Menu model
#         Menu.objects.create(title="IceCream", price=80)
#         Menu.objects.create(title="Burger", price=120)
#         Menu.objects.create(title="Pizza", price=150)

#     def test_getall(self):
#         # Initialize the Django Rest Framework API client
#         client = APIClient()

#         # Make a GET request to the Menu API endpoint
#         response = client.get(reverse('menu-list-create'))  # Adjust the URL pattern name as per your project

#         # Check if the response status code is 200 (OK)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         # Retrieve the serialized data from the response
#         data = response.data

#         # Create a list of expected serialized data for the Menu objects
#         expected_data = [
#             {"title": "IceCream", "price": 80},
#             {"title": "Burger", "price": 120},
#             {"title": "Pizza", "price": 150}
#         ]

#         # Serialize the expected data to JSON for comparison
#         expected_json = json.dumps(expected_data, sort_keys=True)

#         # Serialize the actual data to JSON for comparison
#         data_json = json.dumps(data, sort_keys=True)

#         # Check if the serialized data in the response matches the expected data
#         self.assertEqual(data_json, expected_json)

from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a few test instances of the Menu model
        Menu.objects.create(title="IceCream", price=80)
        Menu.objects.create(title="Burger", price=120)
        Menu.objects.create(title="Pizza", price=150)

    def test_getall(self):
    # Initialize the Django Rest Framework API client
      client = APIClient()

    # Define the URL for the view that lists all Menu objects (adjust this URL)
      url = 'menu-list-create'  # Replace with your actual URL

    # Make a GET request to the view
      response = client.get(url)

    # Check if the response status code is 200 (OK)
      self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Check if the response data is a list
      self.assertIsInstance(response.data, list)

    # Extract titles from the response data and check if they are in expected_menu_titles
      expected_menu_titles = ["IceCream", "Burger", "Pizza"]
      response_menu_titles = [menu.get("title") for menu in response.data]

      for title in expected_menu_titles:
         self.assertIn(title, response_menu_titles)

