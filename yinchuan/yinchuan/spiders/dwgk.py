from asyncio.windows_events import NULL
import scrapy
from yinchuan.items import YinchuanItem

#党务公开
class DwgkSpider(scrapy.Spider):
    name = 'dwgk'
    allowed_domains = ['zjj.yinchuan.gov.cn']
    start_urls = ['http://zjj.yinchuan.gov.cn/dwgk/']

    def parse(self, response):
        item = YinchuanItem()
        item['column'] = '党务公开'
        lists = response.xpath('//div[@class = "larightcon"]/ul/li')
        item['sub_column'] = NULL
        for l in lists:
            item['title'] = l.xpath('./a/@title').get()
            item['href'] = l.xpath('./a/@href').get()
            if item['href'][0] == '.':
                item['href'] = 'http://zjj.yinchuan.gov.cn/dwgk/' + item['href'][2:]
            item['date'] = l.xpath('./span/text()').get().replace('\n','').strip()        

            yield item

        
