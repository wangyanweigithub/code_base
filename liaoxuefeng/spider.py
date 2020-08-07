import os
import bs4
import json
import logging
import requests
import subprocess
from collections import OrderedDict
from lxml import etree
from config import Config


class Spider(object):
    def __init__(self, doc_name, settings=None):
        self.settings = settings() if settings else Config()
        self.doc_name = doc_name
        self._urls = None
        self.log = self.settings.log
        self.info = self.log.info
        self.error = self.log.error
        self.completed = {}

    @property
    def urls(self):
        if self._urls:
            urls = self._urls
        elif os.path.exists(self.settings.url_file[self.doc_name]):
            with open(self.settings.url_file[self.doc_name], 'r') as f:
                urls = json.load(f)
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
                    urls[toc] = {}
                elif ele.tag == 'div':
                    link = ele.xpath(u"a")[0]
                    if link is not None:
                        self.info(ele.tag + "\n" + ele[0].tag + "\n" + ele[0].tag)
                        urls[toc][link.text] = link.attrib["href"]

        self._urls = urls
        print(self._urls)
        with open(self.settings.url_file[self.doc_name], 'w') as f:
            json.dump(self._urls, f)

        self.info(self._urls)

    def get_page(self):
        result = ["# js\n"]
        with open("{}.md".format(self.doc_name), "w") as f:
            for toc, child in self.urls.items():
                    result.append("## {}\n".format(toc))
                    for k, v in child.items():
                        self.info("url is: {}".format(v))
                        url = self.settings.domain + v.strip()
                        page = requests.get(url, headers=self.settings.headers)
                        page = etree.HTML(page.text)
                        contents = page.xpath(u"//div[@id='x-content']")[0]
                        title = contents[0].text
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
                                    result.append("{}. {}\n\n".format(str(p_index), i.text))
                                    p_index += 1
                        except Exception as e:
                            self.error(e)
                            pass
            f.writelines(result)


    def repair_md():
        files = os.listdir(os.getcwd())
        files = [i for i in files if i.endswith(".md")]
        for i in files:
            with open(i, 'r+') as f:
                lines = f.readlines()
                split_num = []
                for k, j in enumerate(lines):
                    if "━━" in j:
                        split_num.append(k)

                print(split_num)
                if len(split_num) >= 2:
                    f.seek(0)
                    f.truncate()
                    title = lines[split_num[0]-3].strip()
                    print("title: ", title)
                    f.writelines(["# ", title, "\n"])
                    f.writelines(lines[split_num[0]+1: split_num[1]])

    def final_file():
        files = os.listdir(os.getcwd())
        files = [i for i in files if i.endswith(".md")]
        with open('js.md', 'w') as f:
            for i in files:
                with open(i, 'r') as j:
                    lines = j.readlines()

                f.writelines(lines)            


spi = Spider("js").get_page()
