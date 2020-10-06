from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime

with open('auth.json') as f:
    auth = json.load(f)
    account_sid = auth['account_sid']
    auth_token = auth['auth_token']
    sender = auth['from_whatsapp_number']
    receiver = auth['to_whatsapp_number']

client = Client(account_sid, auth_token)


product_url = input('Please enter product URL: \n')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}


def price_check():
    price_list = []
    resp = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(resp.content, 'lxml')
    title = (soup.find(id='productTitle').get_text()).strip()
    current_price = float((soup.find(id='priceblock_ourprice').get_text())[1:])
    price_list.append(current_price)
    print(f'Monitoring price of the item below:\n{title}\n')
    while True:
        new_price = float((soup.find(id='priceblock_ourprice').get_text())[1:])
        price_list.append(new_price)
        time_now = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        if price_list[-1] < price_list[0]:
            print(
                f'[ {time_now} ] The long awaited price drop has finally happened!')
            client.messages.create(
                body=f'Price of the item "{title.strip()}" has been reduced to £{price_list[-1]}.\n{product_url}', from_=sender, to=receiver)
            break
        elif price_list[-1] > price_list[0]:
            print(f'[ {time_now} ] You hate it but the price just went up!')
            price_list.pop()
            time.sleep(60)
            continue
        else:
            print(f'[ {time_now} ] Price has not changed...')
            price_list.pop()
            time.sleep(60)
            continue


def main():
    price_check()


if __name__ == '__main__':
    main()
