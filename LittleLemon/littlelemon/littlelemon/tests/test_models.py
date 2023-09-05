from django.test import TestCase
from restaurant.models import Menu


#TestCase class
class MenuTest(TestCase):
  def test_get_item(self):
     item = Menu.objects.create(title="IceCream", price=80)
     itemstr =item.get_item()
     self.assertEqual(itemstr, "IceCream : 80")