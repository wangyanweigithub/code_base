import os
import bs4
import redis
import time
import random
import logging
import requests
import subprocess
from collections import OrderedDict
from lxml import etree
from config import Config


class Spider(object):
    def __init__(self, doc_name, settings=Config):
        self.settings = settings(doc_name)
        self.doc_name = doc_name
        self._urls = None
        self.log = self.settings.log
        self.info = self.log.info
        self.error = self.log.error
        self.completed = {}
        self.redis = redis.StrictRedis()

    @property
    def urls(self):
        if self._urls:
            urls = self._urls
        elif self.redis.get(self.doc_name + "_urls"):
            urls = eval(self.redis.get(self.doc_name + "_urls"))
            self._urls = urls
        else:
            urls = self.get_urls()
        return urls

    def get_urls(self):
        urls = {} 
        page = requests.get(self.settings.root, headers=self.settings.headers)
        page = etree.HTML(page.text)
    
        div = page.xpath(u"//div[@id='{}']/div[@depth='1']".format(self.settings.docs[self.doc_name]))

        for i in div:
            for ele in i:
                if ele.tag == 'a':
                    toc = ele.text
                    urls[toc] = {toc: ele.attrib["href"]}
                elif ele.tag == 'div':
                    link = ele.xpath(u"a")[0]
                    if link is not None:
                        self.info(ele.tag + "\n" + ele[0].tag + "\n" + ele[0].tag)
                        urls[toc][link.text] = link.attrib["href"]
                    depth3 = ele.xpath(u"div[@depth=3]")
                    if depth3:
                        for depth3_div in depth3:
                            depth3_link = depth3_div.xpath(u"a")[0]
                            urls[toc][depth3_link.text] = depth3_link.attrib["href"]

        self._urls = urls
        self.redis.setex(self.doc_name + "_urls", 360, str(self._urls))


    def get_page(self):
        result = ["# {}\n".format(self.doc_name)]
        with open("{}.md".format(self.doc_name), "w") as f:
            self.info(self.urls)
            for toc, child in self.urls.items():
                    result.append("## {}\n".format(toc))
                    for k, v in child.items():
                        self.info("title is {}, url is: {}".format(k, v))
                        url = self.settings.domain + v.strip()
                        self.info("urls is {}".format(url))
                        page = requests.get(url, headers=self.settings.headers)
                        page = etree.HTML(page.text)
                        contents = page.xpath(u"//div[@id='x-content']")[0]
                        title = contents[0].text
                        if title != toc:
                            result.append("### {}\n".format(title))
                        p_index = 1
                        try: 
                            for i in contents[3]:
                                if i.tag.startswith("h"):
                                    result.append("#### {} \n".format(i.text))
                                    p_index = 1
                                elif i.tag == "pre":
                                    result.append("```\n")
                                    for j in i.xpath(u"code"):
                                        result[-1] += j.text
                                    result[-1] += "```\n"
                                else:
                                    p_label = i.xpath("string(.)")
                                    if p_label:
                                        result.append("{}. {}\n\n".format(str(p_index), p_label))
                                        p_index += 1
                        except Exception as e:
                            self.error(e)
                            pass
            f.writelines(result)


spi = Spider("js").get_page()
#spi = Spider("git").get_page()
