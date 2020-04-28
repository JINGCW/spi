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

    start_urls = urls_according_keywords(total_pages=2)

    # print(len(start_urls))
    # for o in start_urls:
    #     print("----------------")
    #     print(o)

    # start_urls = ["http://www.chinastock.com.cn/yhwz_about.do?methodCall=getDetailInfo&docId=7200334"]
    # start_urls = ["https://www.thepaper.cn/newsDetail_forward_7067209"]

    def parse(self, response: scrapy.http.Response):
        # if response.url.startswith("http://www.chinastock.com.cn"):
        #     ps=response.css("div.d_content br")
        # else:
        ps = response.css("p")
        content = ""
        item = XiaoFeiQuanItem()
        item["url"] = response.url
        # item["publish_date"] = re.findall('\d{4}[-/]\d{2}[-/]\d{2}', response.text)[0]
        item["publish_date"] = re.findall('\d{4}-\d{2}-\d{2}', response.text)[0]
        item["news_title"] = response.css("title::text").extract_first().strip()
        # css_pattern = article_css(response.url)
        # print("-------------")
        # print(ps.extract_first())
        # print("-------------")
        for seg in ps:
            # print("-------------")
            # print(seg)
            # print("-------------")
            # words = str(seg.css("p::text").extract_first())
            # words = str(seg.css(css_pattern).extract_first()).strip()
            words = switch_css(seg)
            content += words

        if response.url.__contains__("chinastock.com.cn"):
            # for seg in response.css("div.d_content::text").extract():
            #     print(seg)
            #     content+=seg.strip()
            item["news_content"] = "".join(map(
                lambda x: x.strip().replace("\n", "").replace("\t", "").replace("\r", ""),
                response.css("div.d_content::text").extract()
            ))
        elif response.url.__contains__("thepaper.cn"):
            # for v in response.css("div.news_txt::text").extract():
            #     print(v)
            #     print(type(v))
            #     print('==============')
            item["news_content"] = "".join(map(
                lambda x: x.strip().replace("\n", "").replace("\t", "").replace("\r", ""),
                response.css("div.news_txt::text").extract()
            ))
        else:
            item["news_content"] = content
        yield item
