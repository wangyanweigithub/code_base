import logging


header = """
    Host: www.liaoxuefeng.com
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Cookie: Hm_lvt_2efddd14a5f2b304677462d06fb4f964=1596654718;                                       Hm_lpvt_2efddd14a5f2b304677462d06fb4f964=1596654718; __gads=ID=242401039b053991:T=1596654718:     S=ALNI_MZQnROnQRQ6i0Dsvtdg036VIX0yRA
    Upgrade-Insecure-Requests: 1
    Cache-Control: max-age=0
"""

domain = "https://www.liaoxuefeng.com"


class Config(object):
    def __init__(self, doc_name, *args, **kwargs):
        self.domain = kwargs['domain'] if kwargs.get('domain') else domain
        self.docs= {"js": "1022910821149312", "git": "896043488029600"}
        self.root = kwargs['root'] if kwargs.get('root') else \
            self.domain + "/wiki/" + self.docs[doc_name]
        self._headers = None
        self.logger = logging.getLogger(__name__)
        self.url_file = {"js": "urls.json"}
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)
        fh = logging.FileHandler('spider.log')
        fh.setLevel(logging.ERROR)
        self.log.addHandler(sh)
        self.log.addHandler(fh)

    @property
    def headers(self):
        if self._headers:
            return self._headers

        header_dict = dict([i.strip().split(":", 1) for i in header.strip().split("\n")])
        headers = {k: v.strip() for k, v in header_dict.items()}
        self._headers = headers
        return self._headers


    def get_urls(url):
        urls = []
        page = requests.get(self.root, headers=self.headers)
        dom = bs4.BeautifulSoup(page.text, 'html.parser')
        a_labels = dom.find_all('a', attrs={'href': True})
        for i in a_labels:
            urls.append(i.get("href"))

        get_urls(url)
        urls = [i for i in urls if i.startswith("/wik")]

        with open(js_urls, 'w') as f:
            url_str = "\n".join(urls)
            f.write(url_str)

        return urls


