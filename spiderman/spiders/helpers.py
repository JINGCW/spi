from __future__ import absolute_import, print_function, division

import re
import requests
from urllib.parse import quote
from typing import AnyStr, List, NoReturn
# from twisted.internet import reactor
import time

__all__ = ["urls_according_keywords"]

_headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/6.1 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

_baidu_searcher = r"""https://www.baidu.com/baidu?wd={keyword}&tn=monline_dg&ie=utf-8"""
_download_delay = 0.2


def urls_according_keywords(key_word="消费券",
                            searcher=_baidu_searcher,
                            timeout=10,
                            current_page=0,
                            total_pages=2,
                            key_word_urls_list=None,
                            url=None,
                            s=None
                            ):
    """"""
    if url is None:
        url = searcher.format(keyword=quote(key_word))

    if key_word_urls_list is None:
        key_word_urls_list = []

    if s is None:
        s = _construct_session()

    # print(f"\ntotal_pages is :{total_pages}\n")
    if current_page > total_pages or url is None:
        # print(f"\ncurrent_page > total_pages? {current_page > total_pages}")
        # print(f"url is None? {url is None}\n")
        return key_word_urls_list

    try:
        response = s.request("GET", url, timeout=timeout)
        if response.status_code != 200:
            raise requests.exceptions.RequestException(
                "request {url} state_code is not OK!".format(url=url))

        current_page += 1
        html = response.text
        key_word_urls_list.extend(list(map(lambda x: target_location(s, x), set(re.findall(
            'href\=\"(http\:\/\/www\.baidu\.com\/link\?url\=.*?)\" '
            'class\=\"c\-showurl\"', html)
        ))))
    except Exception as e:
        raise e

    next_url = re.findall(' href\=\"(\/s\?wd\=[\w\d\%\&\=\_\-]*?)\" class\=\"n\"', html)
    # print("--------------------")
    # print(len(next_url))
    # for nu in next_url:
    #     print(nu)
    # print("--------------------")
    next_url = 'https://www.baidu.com' + next_url[-1] if next_url else None
    time.sleep(_download_delay)
    # return reactor.callLater(_download_delay, urls_according_keywords, current_page=current_page,
    #                          key_word_urls_list=key_word_urls_list,
    #                          url=next_url, s=s)
    # print(f"current_page :{current_page}\nnext_url: {next_url}")
    return urls_according_keywords(
        current_page=current_page, key_word_urls_list=key_word_urls_list,
        url=next_url, s=s, total_pages=total_pages)


def request_response():
    return


def target_location(s: requests.Session, origin: AnyStr) -> AnyStr:
    resp = s.request("GET", origin, allow_redirects=False)
    if resp.status_code == 302:
        return resp.headers["location"]

    return origin


def _construct_session():
    s = requests.Session()
    s.headers.update(_headers)
    return s


def article_css(url: AnyStr) -> AnyStr:
    if url.startswith("https://baijiahao.baidu.com") or url.startswith("http://www.topbiz360.com"):
        return "span::text"
    return "p::text"


def switch_css(segment):
    out = segment.css("p::text").extract_first()
    if out is None:
        return str(segment.css("span::text").extract_first()).strip()
    return str(out).strip()
