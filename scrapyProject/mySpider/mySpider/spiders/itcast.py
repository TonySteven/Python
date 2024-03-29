import scrapy

from mySpider.items import TencentItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']

    start_urls = ("http://www.itcast.cn/channel/teacher.shtml",)

    def parse(self, response):
        # open("teacher.html","wb").write(response.body).close()
        # 存放老师信息的集合
        items = []

        for each in response.xpath("//div[@class='main_mask']"):
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = ItcastItem()
            # extract()方法返回的都是字符串
            name = each.xpath("h2/text()").extract()
            print(name)
            title = each.xpath("h2/span/text()").extract()
            print(title)
            info = each.xpath("p/text()").extract()
            print(info)

            # xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            items.append(item)

            yield item

        # 直接返回最后数据
        return items
