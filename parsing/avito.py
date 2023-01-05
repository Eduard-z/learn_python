"""
- .find() и .find_all()
- .find_parent() и find_parents()
- .next_sibling и previous_sibling
- .next_element и previous_element
"""

import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find('div', class_='pagination-pages clearfix')
    pages = divs.find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


def write_csv(data):
    with open('coinmarketcap.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'],
                         data['price'],
                         data['metro'],
                         data['url']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find('div', class_='items-items-kAJAg')
    ads = divs.find_all('div', class_='iva-item-root-_lk9K')
    for ad in ads:
        try:
            div = ad.find('div', class_='title-root-zZCwT').find('h3')
            if 'htc' not in div.text.lower():
                continue
            else:
                title = div.text.strip()
        except:
            title = ''
        try:
            a = ad.find('div', class_='title-root-zZCwT')
            url = "https://avito.ru" + a.find('a').get('href')
        except:
            url = ''
        try:
            price = ad.find('span', itemprop='offers').text.strip()[:-2]
        except:
            price = ''
        try:
            div = ad.find('div', class_='data')
            metro = div.find('span', class_='geo-root-zPwRk').text.strip()
        except:
            metro = ''
        data = {'title': title,
                'price': price,
                'metro': metro,
                'url': url}
        write_csv(data)


def main():
    url = "https://avito.ru/moskva/telefony?p=1&q=htc"
    base_url = "https://avito.ru/moskva/telefony?"
    page_part = "p="
    query_par = "&q=htc"

    # total_pages = get_total_pages(get_html(url))

    for i in range(1, 3):
        url_gen = base_url + page_part + str(i) + query_par
        html = get_html(url_gen)
        get_page_data(html)


if __name__ == '__main__':
    main()
