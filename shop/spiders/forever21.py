# -*- coding: utf-8 -*-
import scrapy
from shop.items import ShopItem

# scraper for any product page on forever21 (works ONLY for f21)
class Forever21Spider(scrapy.Spider):
    name = "forever21"
    allowed_domains = ["forever21.com"]

    # replace start_url with product page
    start_urls = ('http://www.forever21.com/Product/Product.aspx?Br=F21&Category=DRESS&ProductID=2000134198&VariantID=&recid=product_rr-_-2002247963-_-2000134198-_-613-_-1',
    )

# class = "product-title"
    def parse(self, response):
        item = ShopItem()
        item['title'] = response.xpath('//*[@class="product-title"]/text()').extract()
        item['price'] = response.xpath('//*[@class="product-price"]/text()').extract()
        # item['imageUrl'] = response.xpath('//*[@id="ctl00_MainContent_productImage"]').extract()
        # response.css('img').xpath('@src').extract()
        item['imageUrl'] = response.xpath('//*[@id="ctl00_MainContent_productImage"]/@src').extract()

        yield item 
