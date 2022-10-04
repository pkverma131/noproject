import scrapy
import pytz
from datetime import datetime
import json

class ProductsSpider(scrapy.Spider):
    name = "products"

    def start_requests(self):
        urls = [
            'https://www.croma.com/home-appliances/air-conditioners/inverter-acs/c/867'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        product_base_url = 'https://www.croma.com'
        product_list = [{'product_title':j.xpath('./text()').get().replace(chr(160), ' '),'product_link':j.xpath('./@href').get()} for j in response.css('h3.product-title a')]
        products = {'product_base_url':product_base_url,'product_list':product_list}
        filename = str(datetime.now(pytz.timezone("Asia/Calcutta")).strftime('%Y_%m_%d_%H_%M'))+'.json'
        with open(filename, 'w') as fout:
            json.dump(products, fout)
        self.log(f'Saved file {filename}')