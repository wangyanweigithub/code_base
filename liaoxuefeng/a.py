import requests
import os
import subprocess
import bs4
import lxml


url = "https://www.liaoxuefeng.com/wiki/1022910821149312"
domain = "https://www.liaoxuefeng.com"

header = '''
Host: www.liaoxuefeng.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: Hm_lvt_2efddd14a5f2b304677462d06fb4f964=1596654718; Hm_lpvt_2efddd14a5f2b304677462d06fb4f964=1596654718; __gads=ID=242401039b053991:T=1596654718:S=ALNI_MZQnROnQRQ6i0Dsvtdg036VIX0yRA
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
''' 
header_dict = dict([i.strip().split(":", 1) for i in header.strip().split("\n")])
headers = {k: v.strip() for k, v in header_dict.items()}
js_urls = './js_urls'

def get_urls(url):
    urls = []
    page = requests.get(url, headers=headers)
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


def get_page():

    if os.path.exists(js_urls ):
        print("js_urls completed generate")

    with open(js_urls, 'r') as f:
        urls = f.readlines()

    for k, i in enumerate(urls):
        url = domain + i.strip()
        with open(str(k)+".md", 'w') as f:
            res = subprocess.Popen(['w3m', url], stdout=f)


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
        

