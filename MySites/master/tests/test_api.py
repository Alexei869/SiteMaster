# Импорт функций и пакетов
from django.urls import reverse
from rest_framework.test import APITestCase


# Тесты
class MasterApiTestCase1(APITestCase):
    def test_get(self):
        url = reverse('master-home')
        print(url)
        response = self.client.get(url)
        print(response)


class MasterApiTestCase2(APITestCase):
    def test_get(self):
        url = reverse('master-about')
        print(url)
        response = self.client.get(url)
        print(response)
