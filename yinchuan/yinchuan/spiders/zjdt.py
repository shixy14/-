from asyncio.windows_events import NULL
import scrapy
from yinchuan.items import YinchuanItem

#住建动态
class ZjdtSpider(scrapy.Spider):
    name = 'zjdt'
    allowed_domains = ['zjj.yinchuan.gov.cn']
    start_urls = ['http://zjj.yinchuan.gov.cn/zjdt/']

    def parse(self, response):
        item = YinchuanItem()
        item['column'] = '住建动态'
    
        lists = response.xpath('//div[@class = "larightcon"]/ul/li')
        item['sub_column'] = NULL
        for l in lists:
            
            item['title'] = l.xpath('./a/@title').get()

            item['href'] = l.xpath('./a/@href').get()
            if item['href'][0] == '.':
                item['href'] = 'http://zjj.yinchuan.gov.cn/zjdt/' + item['href'][2:]
            item['date'] = l.xpath('./span/text()').get().replace('\n','').strip()        
           
            yield item

