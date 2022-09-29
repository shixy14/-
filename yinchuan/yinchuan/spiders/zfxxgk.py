from asyncio.windows_events import NULL
import imp
from tkinter import Y
import scrapy
from yinchuan.items import YinchuanItem

#政府信息公开
class ZfxxgkSpider(scrapy.Spider):
    name = 'zfxxgk'
    allowed_domains = ['zjj.yinchuan.gov.cn']
    start_urls = ['http://zjj.yinchuan.gov.cn/']

    base_site = 'http://zjj.yinchuan.gov.cn/'
    column = ''
    def parse(self, response):
        item = YinchuanItem()
        
        self.column = response.xpath('//div[@class = "left1"]/div[@class = "title"]/a/text()').extract_first()
        book_urls = response.xpath('//div[@class = "left1"]/div[@class = "con1"]/div[@class = "titlex"]//a/@href').extract()
        for book_url in book_urls:
           url = self.base_site +  book_url[2:]
           yield scrapy.Request(url, callback = self.get_info)

        
        
    def get_info(self, response): 
        item = YinchuanItem()
        item['column'] = self.column
        item['sub_column'] = response.xpath('//div[@class="zfxxgk_zdgktit"]/a/text()').extract_first()
        lists = response.xpath('//div[@class="zfxxgk_zdgkc"]/ul/li')
        for l in lists:
            #分三个子栏目 文件通知、人事任免、预决算公开
            item['title'] = l.xpath('./a/@title').get()
            item['href'] = l.xpath('./a/@href').get()
            
            if item['href'][0] == '.':
                item['href'] = response.url + item['href'][2:]
            #datetime 格式有问题
            item['date'] = l.xpath('./b/text()').get().replace('\n','').strip()  
            
            #print(item['column'])
            
            yield item

