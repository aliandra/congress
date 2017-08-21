import scrapy


class RepSpider(scrapy.Spider):
    name = 'reps'

    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "CONCURENT_REQUESTS_PER_DOMAIN": 1,
        "HTTPCASHE_ENABLED": True
    }

    start_urls = [
        "http://www.house.gov/representatives/"
    ]

    def parse(self, response):
        tables = response.xpath('.//div[@id="byName"]/table')
        for rep in tables.xpath('.//tbody/tr'):
            yield{
                'name': rep.xpath('.//td[1]/a/text()').extract_first(),
                'website': rep.xpath('.//td[1]/a/@href').extract(),
                'district': rep.xpath('.//td[2]/text()').extract_first(),
                'party': rep.xpath('.//td[3]/text()').extract_first(),
                'room': rep.xpath('.//td[4]/text()').extract_first(),
                'phone': rep.xpath('.//td[5]/text()').extract_first(),
                'committee': rep.xpath('.//td[6]/text()').extract()
            }
