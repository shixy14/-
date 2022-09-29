from asyncio.windows_events import NULL
import scrapy
from yinchuan.items import YinchuanItem

#住房保障公示
class ZfbzgsSpider(scrapy.Spider):
    name = 'zfbzgs'
    allowed_domains = ['zjj.yinchuan.gov.cn']
    start_urls = ['http://zjj.yinchuan.gov.cn/zwgk/fdzdgknr/gsgg/zfbzgs/']

    def parse(self, response):
        item = YinchuanItem()
        item['column'] = response.xpath('//div[@class="zfxxgk_zdgktit"]/a/text()').extract_first()
        
        item['sub_column'] = NULL
        lists = response.xpath('//div[@class="zfxxgk_zdgkc"]/ul/li')
        for l in lists:
            
            item['title'] = l.xpath('./a/@title').get()
            item['href'] = l.xpath('./a/@href').get()
            
            if item['href'][0] == '.':
                item['href'] = 'http://zjj.yinchuan.gov.cn/zwgk/fdzdgknr/gsgg/zfbzgs/' + item['href'][2:]
            #datetime 格式有问题
            item['date'] = l.xpath('./b/text()').get().replace('\n','').strip()  
            
            #print(item['column'])
            
            yield item
