from asyncio.windows_events import NULL
import scrapy
from yinchuan.items import YinchuanItem

#政策法规
class ZcfgSpider(scrapy.Spider):
    name = 'zcfg'
    allowed_domains = ['zjj.yinchuan.gov.cn']
    start_urls = ['http://zjj.yinchuan.gov.cn/zcfg/']

    def parse(self, response):
        item = YinchuanItem()
        item['column'] = '政策法规'
        lists = response.xpath('//div[@class = "larightcon"]/ul/li')
        item['sub_column'] = NULL
        for l in lists:
            item['title'] = l.xpath('./a/@title').get()
            item['href'] = l.xpath('./a/@href').get()
            if item['href'][0] == '.':
                item['href'] = 'http://zjj.yinchuan.gov.cn/zcfg/' + item['href'][2:]
            item['date'] = l.xpath('./span/text()').get().replace('\n','').strip()        

            yield item
