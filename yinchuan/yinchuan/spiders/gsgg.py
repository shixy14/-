import scrapy
from yinchuan.items import YinchuanItem

#公示公告
class GsggSpider(scrapy.Spider):
    name = 'gsgg'
    allowed_domains = ['zjj.yinchuan.gov.cn']
    #start_urls = ['http://zjj.yinchuan.gov.cn/']
    start_urls = ['http://zjj.yinchuan.gov.cn/zwgk/fdzdgknr/gsgg/']
    
    def parse(self, response):
        item = YinchuanItem()
        item['column'] = '公示公告'
        lists1 = response.xpath('//div[@class="zfxxgk_zdgktit"]')
        lists2 = response.xpath('//div[@class="zfxxgk_zdgkc"]/ul/li')
        
        titles = lists2.xpath('./a/@title').extract()
        hrefs = lists2.xpath('./a/@href').extract()
        dates = lists2.xpath('./b/text()').extract()

        count = 0
        for l1 in lists1:
            item['sub_column'] = l1.xpath('./a/text()').get()
            for i in range(0,5):
                item['title'] = titles[count]
                item['href'] = hrefs[count]
                
                if item['href'][0] == '.':
                    item['href'] = 'http://zjj.yinchuan.gov.cn/zwgk/fdzdgknr/gsgg/' + item['href'][2:]
                item['date'] = dates[count]
                count += 1
                if(count % 5) == 0:
                    break
                yield item
                
            #print(item['column'])

            yield item

        

            

