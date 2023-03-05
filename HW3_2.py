import requests
from pprint import pprint
import pathlib
from pathlib import Path


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self.get_upload_link(disk_file_path=filename).get("href", "")
        with open(disk_file_path, 'rb') as file:
            response = requests.put(href, files={"file": file})
            response.raise_for_status()
        if response.status_code == 201:
            print("Файл загружен")


if __name__ == '__main__':
    file_name = 'test.txt'
    path_to_file = str(Path(pathlib.Path.cwd(), file_name))
    token = ""
    uploader = YaUploader(token=token)
    uploader.upload_file_to_disk(path_to_file, file_name)
