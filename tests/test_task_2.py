import unittest
import requests
from YaDisk import YaDisk


class TestYaDiskFunctions(unittest.TestCase):
    def setUp(self):
        self.ya_token = ''  # Введите ваш токен с полигона REST API Я.Диска
        self.ya_client = YaDisk(self.ya_token)
        self.f_name = 'new_folder'
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.ya_token)
        }
        self.params = {'path': 'disk:/'}

    def test_folder_creation(self):
        test_case = {
                'folder_name': self.f_name,
                'exp_result': 201
            }
        result = self.ya_client.create_folder(test_case['folder_name'])
        self.assertEqual(test_case['exp_result'], result)

    def test_folder_creation_fail(self):
        test_case = {
                'folder_name': self.f_name,
                'exp_result': 201
            }
        result = self.ya_client.create_folder(test_case['folder_name'])
        self.assertNotEqual(test_case['exp_result'], result)

    def test_folder_existence(self):  # Проверка наличия папки по метаинформации о содержимом корневого каталога
        response = requests.get(self.url, headers=self.headers, params=self.params)
        result = None
        for element in response.json()['_embedded']['items']:
            if element['type'] == 'dir' and element['name'] == self.f_name:
                result = True
                break
            else:
                result = False
        self.assertTrue(result)

    def test_folder_existence_2(self):  # Проверка наличия папки по ответу на запрос по имени папки
        params = {'path': self.f_name}
        response = requests.get(self.url, headers=self.headers, params=params)
        result = response.status_code
        self.assertEqual(200, result)


if __name__ == '__main__':
    unittest.main()
