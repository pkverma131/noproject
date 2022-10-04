import json
import requests
import pytz
from datetime import datetime


API_URL = "https://api.croma.com/product/allchannels/v1/category/867?currentPage={page}&query=:relevance:excludeOOSFlag&fields=FULL&sort=relevance"

def get_products(api_url):
    product_list = []
    payload={}
    headers = {}
    page_count = 0
    while True:
        print('page number'+(str(page_count)))
        url = api_url.format(page=str(page_count))
        response = requests.request("GET", url, headers=headers, data=payload)
        result = json.loads(response.text)
        products = result['products']
        if len(products)>0:
            product_list.extend(products)
            page_count+=1
        else:
            break
    filename = str(datetime.now(pytz.timezone("Asia/Calcutta")).strftime('%Y_%m_%d_%H_%M'))+'.json'
    with open(filename, 'w') as fout:
            json.dump(product_list, fout)

get_products(API_URL)