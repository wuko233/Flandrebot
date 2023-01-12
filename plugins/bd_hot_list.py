import requests
from bs4 import BeautifulSoup
def show():
    text = "百度热搜：\n"
    url = "https://top.baidu.com/board"
    pre = {'User-agent':'Mozilla/5.0'}
    res = requests.get(url, headers = pre)
    rep = res.text
    soup = BeautifulSoup(rep,"html.parser")
    hot_top = soup.find(class_ = "list_1EDla") #热搜榜
    for search_one in hot_top.find_all('a', class_ = "item-wrap_2oCLZ"):
        search_title = search_one.find(class_ = "c-single-text-ellipsis")
        text = text + search_title.text + "\n"
    return text