import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

BITLINK_ENDPOINT = 'https://api-ssl.bitly.com/v4/bitlinks'


def parsed_link(url):
    url_parsed = urlparse(url)
    return str(url_parsed._replace(scheme='').geturl()).replace('//', '')


def shorten_link(token, url):
    payload = {'long_url': url}
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(BITLINK_ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    url_bitlink = f'{BITLINK_ENDPOINT}{url}/clicks/summary'
    response = requests.get(url_bitlink, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    url_bitlink_info = f'{BITLINK_ENDPOINT}{url}'
    response = requests.get(url_bitlink_info, headers=headers)
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['BITLINK_TOKEN']
    user_url = input('Введите ссылку: ')
    if not is_bitlink(token, parsed_link(user_url)):
        print('Битлинк', shorten_link(token, user_url))
    else:
        print(f'По вашей ссылке прошли '
              f'{count_clicks(token, parsed_link(user_url))} раз(а)')
