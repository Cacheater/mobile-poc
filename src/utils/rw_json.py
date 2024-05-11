import json
import pytest

from utils.initialize import Initialize


class GetJson:
    def __init__(self):
        self.json_strings = None

    def get_json_file(self):
        json_path = Initialize.DEVICES_JSON
        print("Json path " + json_path)
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                print("get_json_file: " + json_path)
        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"get_json_file: No se encontro el Archivo: devices.json")

    def get_device(self, device):
        if self.json_strings is False:
            print("Define el DOM para esta prueba")
        else:
            try:
                self.json_strings[device]
                return self.json_strings[device]

            except KeyError:
                pytest.skip(u"fn_get_device: No se encontro el dispositivo: " + device)
                return None