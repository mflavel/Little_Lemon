from django.test import TestCase
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu
from rest_framework import status


class MenuTestCase(TestCase):
    def test_item(self):
        item = Menu.objects.create(
            title="Test Dish",
            price=9.99,
            inventory=10
        )
        self.assertEqual(str(item), "Test Dish : 9.99")

class MenuViewTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(title="Dish 1", price=5.00, inventory=20)
        Menu.objects.create(title="Dish 2", price=10.00, inventory=15)

    def test_getall(self):
        response = self.client.get('/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)