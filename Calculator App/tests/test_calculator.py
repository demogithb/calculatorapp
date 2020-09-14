import requests
from bs4 import BeautifulSoup
import pytest


url = "http://127.0.0.1:5000/send"

input_to_test_calculator = ['3;4;add;7.0',
                            '13.45;4.45;add;17.90',
                            '13.50;5.50;add;19.0',
                            '13.46;4;add;17.46',
                            '0;0;add;0.0',
                            '2;6;add;7',
                            '13;5;subtract;8.0',
                            '11.5;1;subtract;10.5',
                            '0;0;subtract;0.0',
                            '12.25;2.12;subtract,10.13',
                            '12;7;subtract;4',
                            '3;4;multiply;12.0',
                            '3.5;2.5;multiply;8.75',
                            '3.5;4;multiply;14.0',
                            '3;2.29;multiply;6.87',
                            '4;5;multiply;19',
                            '12;4;divide;3.0',
                            '12.5;4;divide;3.125',
                            '12.4;4;divide;3.1',
                            '0;5;divide;0.0',
                            '0;0.0;divide;Zero Division Error :Sorry ! You are dividing by zero',
                            'ses;5.0;add;Value Error :Input should be numeric',
                            'ses;ses;subtract;Value Error :Input should be numeric',
                            'ses;5.0;multiply;Value Error :Input should be numeric',
                            'ses;5.0;divide;Value Error :Input should be numeric',
                            ]


@pytest.mark.parametrize("input_to_test_calculator", input_to_test_calculator)
def test_calculator(input_to_test_calculator):
    num1, num2, operation, result = input_to_test_calculator.split(';')
    payload = {'num1': num1, 'num2': num2, 'operation': operation}
    response = requests.post(url, data=payload)
    parsed_html = BeautifulSoup(response.text, 'html.parser')
    parsed_html_result = parsed_html.body.find('div', attrs={'class': 'alert'}).text
    # print(payload)
    # print(response.text)
    # print(parsed_html_result)
    # print(response.headers)
    assert parsed_html_result == result
    # assert result[1689:1693] == '46.00'
