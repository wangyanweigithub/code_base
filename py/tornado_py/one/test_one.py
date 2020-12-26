import requests
import pytest


class TestInput(object):

    def setup_class(self):
        self.url = "http://127.0.0.1:8888"
        self.data = {"name": "wang", "name": "yan"}

    def teardown_class(self):
        pass

    def test_get(self):
        res = requests.get(self.url, params=self.data)
        print(res.text)

    def test_post_params(self):
        res = requests.post(self.url, params=self.data)
        print(res.text)

    def test_post_data(self):
        res = requests.post(self.url, data=self.data)
        print(res.text)


if __name__ == "__main__":
    pytest.main(["-s", "test_one.py"])
