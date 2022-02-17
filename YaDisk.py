import requests


class YaDisk:
    url = "https://cloud-api.yandex.net"

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, f_name):
        folder_url = self.url + '/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': f_name}
        response = requests.put(folder_url, headers=headers, params=params)
        return response.status_code


if __name__ == '__main__':
    ya_token = ''  # Введите ваш токен с полигона REST API Я.Диска
    ya_client = YaDisk(ya_token)
    ya_client.create_folder('Oops')
