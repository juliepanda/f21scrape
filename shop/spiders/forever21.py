# -*- coding: utf-8 -*-
import scrapy


class Forever21Spider(scrapy.Spider):
    name = "forever21"
    allowed_domains = ["forever21.com"]
    start_urls = ('http://www.forever21.com/Product/Product.aspx?BR=f21&Category=dress&ProductID=2002247963&VariantID=',
    )
# class = "product-title"
    def parse(self, response):
        title = response.xpath('//title').extract()
        print title
        
