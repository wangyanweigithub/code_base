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

root = "https://www.liaoxuefeng.com/wiki/1022910821149312"

domain = "https://www.liaoxuefeng.com"


class config(object):
    def __init__(self, *args, **kwargs):
        self.root = kwargs['root'] if kwargs.get('root') else root
        self.domain = kwargs['domain'] if kwargs.get('domain') else domain
        self.header = None

    @property
    def headers(self):
        if self.headers:
            return self.headers

        header_dict = dict([i.strip().split(":", 1) for i in header.strip().split("\n")])
        headers = {k: v.strip() for k, v in header_dict.items()}
        self.headers = headers
        return header


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


