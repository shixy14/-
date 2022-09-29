from asyncio.windows_events import NULL
import scrapy
from yinchuan.items import YinchuanItem

#培训教育
class PxjySpider(scrapy.Spider):
    name = 'pxjy'
    allowed_domains = ['zjj.yinchuan.gov.cn']
    start_urls = ['http://zjj.yinchuan.gov.cn/pxjy/']

    def parse(self, response):
        item = YinchuanItem()
        item['column'] = '培训教育'
        lists = response.xpath('//div[@class = "larightcon"]/ul/li')
        item['sub_column'] = NULL
        for l in lists:
            item['title'] = l.xpath('./a/@title').get()
            item['href'] = l.xpath('./a/@href').get()
            if item['href'][0] == '.':
                item['href'] = 'http://zjj.yinchuan.gov.cn/pxjy/' + item['href'][2:]
            item['date'] = l.xpath('./span/text()').get().replace('\n','').strip()        

            yield item