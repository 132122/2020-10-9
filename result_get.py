from bs4 import BeautifulSoup
import requests
import pyspider

def get_html(url):
    response = requests.get(url)
    response.encoding = "UTF-8"
    if response.status_code == 200:
        return response.text
    else:
        print("链接错误")

def main():
    url = "https://www.cdp.edu.cn/Category_2023/Index.aspx"
    html = get_html(url)
    soup = BeautifulSoup(html,"html.parser")
    for item in soup.find_all("a"):
        print(item.get("href"))

if __name__ == '__main__':
    main()