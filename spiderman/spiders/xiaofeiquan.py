from ..items import XiaoFeiQuanItem
import re
import scrapy
from .helpers import urls_according_keywords, article_css, switch_css


class XiaoFeiQuanSpider(scrapy.Spider):
    name = "xiaofeiquan"
    # allowed_domains = ['finance.ifeng.com']
    # start_urls = [
    #     "http://finance.ifeng.com/c/7v8S9kxcqwa",
    #     "http://www.sx.gov.cn/art/2020/4/11/art_1462938_42552885.html"
    # ]

    # start_urls = urls_according_keywords(total_pages=20)

    # print(len(start_urls))
    # for o in start_urls:
    #     print(o)

    start_urls = ["http://www.chinastock.com.cn/yhwz_about.do?methodCall=getDetailInfo&docId=7200334"]

    def parse(self, response: scrapy.http.Response):
        ps = response.css("p")
        content = ""
        item = XiaoFeiQuanItem()
        item["url"] = response.url
        # item["publish_date"] = re.findall('\d{4}[-/]\d{2}[-/]\d{2}', response.text)[0]
        item["publish_date"] = re.findall('\d{4}-\d{2}-\d{2}', response.text)[0]
        item["news_title"] = response.css("title::text").extract_first().strip()
        # css_pattern = article_css(response.url)
        print("-------------")
        print(ps)
        print("-------------")
        for seg in ps:
            print("-------------")
            print(seg)
            print("-------------")
            # words = str(seg.css("p::text").extract_first())
            # words = str(seg.css(css_pattern).extract_first()).strip()
            words = switch_css(seg)
            content += words

        item["news_content"] = content
        yield item
