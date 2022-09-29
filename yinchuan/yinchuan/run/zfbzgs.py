from scrapy import cmdline
print('住房保障公示')
cmdline.execute("scrapy crawl zfbzgs".split())