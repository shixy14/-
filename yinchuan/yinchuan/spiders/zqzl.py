from asyncio.windows_events import NULL
import scrapy
from yinchuan.items import YinchuanItem

#专区专栏
class ZqzlSpider(scrapy.Spider):
    name = 'zqzl'
    allowed_domains = ['zjj.yinchuan.gov.cn']
    start_urls = ['http://zjj.yinchuan.gov.cn/']

    base_site = 'http://zjj.yinchuan.gov.cn/'
    column = ''
    def parse(self, response):
        item = YinchuanItem()
        
        self.column = response.xpath('//div[@class = "part3"]/div[@class = "left"]/div[@class = "title"]/div[@class = "titlel"]/text()').extract_first()
        book_urls = response.xpath('//div[@class = "part3"]/div[@class = "left"]/div[@class = "con"]/div[@class = "titlex"]//a/@href').extract()
        for book_url in book_urls:
           url = self.base_site +  book_url[2:]
           yield scrapy.Request(url, callback = self.get_info)
  
     
    def get_info(self, response):
        
        item = YinchuanItem()
        item['column'] = self.column
        titles = response.xpath('//div[@class="larightnav"]/a/text()').extract()
        item['sub_column'] = titles[2]

        lists = response.xpath('//div[@class = "larightcon"]/ul/li')
        for l in lists:
            item['title'] = l.xpath('./a/@title').get()
            item['href'] = l.xpath('./a/@href').get()
            if item['href'][0] == '.':
                item['href'] = response.url + item['href'][2:]
            item['date'] = l.xpath('./span/text()').get().replace('\n','').strip()        

            yield item

        
