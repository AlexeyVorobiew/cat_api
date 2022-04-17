import pytest
import requests
import allure
from requests.exceptions import HTTPError

class requestCore():
    def __init__(self, domain):
        self.domain = domain

    def GET(self, path, headers):
        try:
            url = f'{self.domain}{path}'
            print(url)
            with allure.step(f'GET request to: {url}'):
                return requests.get(url, headers)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')

    def POST(self, path, data=None, json=None, headers=None):

        try:
            url = f'{self.domain}{path}'
            print(url)
            with allure.step(f'POST request to: {url}'):
                return requests.post(url=url, data=data, json=json, headers=headers)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')



@pytest.fixture(scope="session")
def api_request():
    return requestCore(domain='https://api.thecatapi.com')
