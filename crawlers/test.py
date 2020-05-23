import requests
from bs4 import BeautifulSoup


def getHTTP(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/80.0.3987.149 Safari/537.36'}
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # 当采用beautiful soup库时，其判断当前文本的编码方式与实际编码方式不同
        # 一个是在HTTP过程中的utf-8，一个是在windows下的编码格式
        return r.text

    except:
        if r.status_code == 418:
            return "I'm a teapot"
        else:
            return "Error"


if __name__ == "__main__":
    url = "https://movie.douban.com/top250"
    demo = getHTTP(url)
    soup = BeautifulSoup(demo, "html.parser")
    soup.prettify()

    # print(soup.prettify())
    # print(demo)

# print(r.status_code)
# r.encoding = 'utf-8'
# print(r.text)
# print(type(r))
# print(r.headers)

