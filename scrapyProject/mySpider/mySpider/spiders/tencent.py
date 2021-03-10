import re

import scrapy


class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["careers.tencent.com"]
    start_urls = [
        "https://careers.tencent.com/search.html?index=1"
    ]

    def parse(self, response):

        items = response.xpath("//a[@class='recruit-list-link']")
        for item in items:
            temp = dict(
                name=item.xpath("h4/text()").extract()[0],
                # detailLink="http://hr.tencent.com/jobdesc.html?postId=" + item.xpath("@href").extract()[0],
                positionInfo=item.xpath('p[2]/text()').extract()[0] if len(
                    item.xpath('p[2]/text()').extract()) > 0 else None,
                # peopleNumber=item.xpath('./td[3]/text()').extract()[0],
                workLocation=item.xpath('p[1]/span[2]/text()').extract()[0],
                publishTime=item.xpath('p[1]/span[4]/text()').extract()[0]
            )
            print("temp===============" + temp)

            yield temp

        now_page = int(re.search(r"\d+", response.url).group(0))
        print("*" * 100)
        if now_page < 9:
            url = re.sub(r"\d+", str(now_page + 1), response.url)
            print("this is next page url:", url)
            print("*" * 100)

            yield scrapy.Request(url, callback=self.parse)
