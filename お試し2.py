import requests as requests
from bs4 import BeautifulSoup

url = "https://tabelog.com/tokyo/A1301/A130103/R5266/rstLst/?vs=1&sa=%E6%96%B0%E6%A9%8B%E9%A7%85&sk=%25E5%2580%258B%25E5%25AE%25A4&lid=hd_search1&vac_net=&svd=20200323&svt=1900&svps=2&hfc=1&ChkRoom=1&cat_sk=%E5%80%8B%E5%AE%A4"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# tags = soup.find_all("a", class_="list-rst__rst-name-target cpy-rst-name")
# for i in tags:
# print('name:{} url:{}'.format(i.text, i.get("href")))

restrants = soup.find_all("div", class_="list-rst__wrap js-open-new-window")

for r in restrants:
    print(r.find("a").text, r.a.get("href"))
