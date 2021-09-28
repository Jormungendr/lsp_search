from bs4 import BeautifulSoup
import requests
import os
def lsp_search():
    front = "https://www.xiurenji.cc"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

    f1 = open('./test.txt', "w+")
    search = input("请输入关键字：")
    if search != '继续':
        search = str(search.encode('gb2312')).replace('\\x', '%').replace('\'', '')[1:]
        for page in range(1, 20):
            search_url = 'https://www.xiurenji.cc/plus/search/index.asp?keyword='+str(search)+'&searchtype=title&p=' \
                        + str(page)
            url_soup = BeautifulSoup(requests.get(search_url, headers=header).content.decode("gb2312", "ignore").
                                    encode("utf-8", "ignore"), 'html.parser')
            search_all = url_soup.find_all(name='div', attrs={"class": "title1"})
            print(search_url)
            if len(search_all) > 1:
                for a in search_all:
                    print(a)
                    f1.write(front + str(a)[29:46] + '\n')
            else:
                break
        f1.close()

    f1 = open('./test.txt')
    lines = f1.readlines()
    for url in lines:
        path = './' + str(url.replace('.html', '').replace('https://www.xiurenji.cc/MFStar/', '')
                        .replace('https://www.xiurenji.cc/MyGirl/', '').replace('https://www.xiurenji.cc/MiStar/', '')
                        .replace('https://www.xiurenji.cc/MiiTao/', '').replace('https://www.xiurenji.cc/DKGirl/', '')
                        .replace('https://www.xiurenji.cc/YouMi/', '').replace('https://www.xiurenji.cc/FeiLin/', '')
                        .replace('https://www.xiurenji.cc/BoLoli/', '').replace('https://www.xiurenji.cc/IMiss/', '')
                        .replace('https://www.xiurenji.cc/YouWu/', '').replace('https://www.xiurenji.cc/XingYan/', '')
                        .replace('https://www.xiurenji.cc/XiaoYu/', '')
                        .replace('https://www.xiurenji.cc/XiuRen/', '').replace('\n', '')).replace('"','') + '/'
        os.makedirs(path, exist_ok=True)
        for tmp in range(0, 91):
            if tmp > 0:
                tmp_url = str(url.replace('.html', '_').replace('\n', '')) + str(tmp) + '.html'
            else:
                tmp_url = url.replace('\n', '')
            print(tmp_url)
            url_soup = BeautifulSoup(requests.get(tmp_url, headers=header).content.decode("gb2312", "ignore").
                                    encode("utf-8", "ignore"), 'html.parser')
            all_a = url_soup.find_all('img')

            if len(all_a) > 3:
                for a in all_a:
                    print(a['src'])
                    try:
                        r = requests.get(front+a['src'])
                        if len(a['src'][-15:]) == 15 and a['src'][-3:] == 'jpg':
                            with open(path+a['src'][-15:].replace('le/pic/', ''), 'wb') as f:
                                f.write(r.content)
                    except requests.exceptions.SSLError:
                        s = requests.session()
                        s.keep_alive = False
                        continue
            else:
                break
