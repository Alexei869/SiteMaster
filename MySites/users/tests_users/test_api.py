# Импорт функций и пакетов
from django.urls import reverse
from rest_framework.test import APITestCase


# Тесты
class MasterApiTestCase3(APITestCase):
    def test_get(self):
        url = reverse('login')
        print(url)
        response = self.client.get(url)
        print(response)


class MasterApiTestCase4(APITestCase):
    def test_get(self):
        url = reverse('logout')
        print(url)
        response = self.client.get(url)
        print(response)


class MasterApiTestCase5(APITestCase):
    def test_get(self):
        url = reverse('profile')
        print(url)
        response = self.client.get(url)
        print(response)


class MasterApiTestCase6(APITestCase):
    def test_get(self):
        url = reverse('register')
        print(url)
        response = self.client.get(url)
        print(response)

