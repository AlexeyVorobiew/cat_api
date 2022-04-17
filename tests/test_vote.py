import pytest
import allure
from data_for_test import key_header

@allure.feature('votes search')
@allure.story('Тест голосовалки. Негативный сценарий. Пустое image_id')
def test_vote(api_request):
    json = {}
    response = api_request.POST(path="/v1/votes/", headers=key_header,json=json)
    with allure.step("Запрос отправлен. Негативный сценарий с пустым json"):
        assert response.status_code == 400





