import random
import time

import requests
import os
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 "
                      "Safari/537.36 Edg/118.0.2088.46"}

    # 获取当前页面内容  返回四大名著标题和url
    response = requests.get(url, headers=headers)
    response.encoding = "UTF-8"
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_book(soup):
    div = soup.find_all('div', class_="book-item")
    book_dic = {}
    for con in div:
        book_name = con.get_text().replace('\n', '')
        book_href = 'https://www.shicimingju.com' + con.a['href']
        # print(book_name)
        # print(book_href)
        book_dic[book_name] = book_href
    return book_dic


def get_book_mulu(book_html):
    '''
    抓取四大名著的章节 标题和url
    :param book_html:
    :return:
    '''
    # 包含了整个章节的div
    div = book_html.find_all('div', class_='book-mulu')
    # 存储章节标题和url的字典
    mulu_dict = {}  # {章节:url}
    for d in div:
        # 抓取超链接
        mulu_hrefs = d.find_all('a')
        for mulu_href in mulu_hrefs:
            title = mulu_href.get_text()
            herf = mulu_href['href']
            mulu_dict[title] = 'https://www.shicimingju.com' + herf
    return mulu_dict


def book_mulu_content(chapter, books_html):
    con_dic = {}
    div = books_html.find('div', class_='chapter_content')
    text = div.text
    con_dic[chapter] = text
    return con_dic


def save_books(book_name, book_contents):
    if not os.path.exists(book_name):
        os.mkdir(book_name)
    for title in book_contents:
        path = os.path.join(book_name, title + '.text')
        with open(path, 'w', encoding='UTF-8') as f:
            f.write(book_contents[title])
            print(f'{book_name} === {title} 下载完成!!!!!')


def main(main_url):
    soup = get_html(main_url)
    book_dic = get_book(soup)
    for book_name in book_dic:
        mulu_dic = get_book_mulu(get_html(book_dic[book_name]))
        for title, url in mulu_dic.items():
            # 获取章节内容
            book_contents = book_mulu_content(title, get_html(url))
            save_books(book_name, book_contents)
            time.sleep(random.randint(2, 3))


if __name__ == '__main__':
    main_url = 'https://www.shicimingju.com/bookmark/sidamingzhu.html'
    main(main_url)
