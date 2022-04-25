"""
pip install requests
pip install beautifulsoup4
pip install lxml
"""

import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool


def get_html(url):
    response = requests.get(url)  # объект класса Response
    return response.text          # возвращает HTML-код страницы


def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    tds = soup.find('tbody').find_all('td', class_='cmc-table__cell--sort-by__name')
    links = []
    for td in tds:
        a = td.find('a').get('href')            # string
        link = 'https://coinmarketcap.com' + a  # e.g. href="/currencies/bitcoin/"
        links.append(link)
    return links


def text_before_word(text, word):
    line = text.split(word)[0].strip()
    return line


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        name = text_before_word(soup.find('title').text, 'price')
    except:
        name = ''
    try:
        price = text_before_word(soup.find('div', 
class_='col-xs-6 col-sm-8 col-md-4 text-left').text, 'USD')
    except:
        price = ''
    data = {'name': name,
            'price': price}
    return data


def write_csv(data):
    with open('coinmarketcap.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['price']))
        print(data['name'], ' - ', data['price'], 'parsed')


def make_all(link):
    html = get_html(link)
    data = get_page_data(html)
    write_csv(data)


def main():
    start = datetime.now()
    url = 'https://coinmarketcap.com/all/views/all'
    all_links = get_all_links(get_html(url))

    with Pool(40) as p:
        p.map(make_all, all_links)

    #for i, link in enumerate(all_links):
    #    html = get_html(link)
    #    data = get_page_data(html)
    #    write_csv(i, data)
        
    end = datetime.now()
    total = end - start
    print(str(total))
    a = input()

if __name__ == '__main__':
    main()
    