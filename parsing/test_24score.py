import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver

def get_html(url):
    req = requests.get(url)
    return req.text

def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', class_='t1 matches').find_all('tr')
    links = []
    for tr in trs:
        tour_text = tr.find('td', colspan='4').text
        date_text = tr.find('td', class_='date').text
        team1_text = tr.find('td', class_='w25p left').text
        links.append((tour_text, date_text, team1_text))
        print(links)
        break
    return links

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

def main():
    start = datetime.now()
    url = 'https://24score.pro/football/belarus/premier_league/2020/regular_season/fixtures/'
    browser = webdriver.Chrome()
    browser.get(url)
    trs = browser.find_elements_by_xpath('//table//tr/td')
    print(len(trs))

    count = 1
    for i in trs:
    	game = "game_" + count
    	if i.get_attribute('colspan') is not None:
    		tour_text = i.text
    	elif i.get_attribute('class') == "date":
    		date_text = i.text
    	elif i.get_attribute('class') == "w25p left":
    		team_text = i.text
    	elif i.get_attribute('class') == "score":
    		score_text = i.text

    		print(i.get_attribute('colspan'))
    #all_links = get_all_links(get_html(url))

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
    