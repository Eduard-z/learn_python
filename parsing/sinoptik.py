import requests, bs4

s=requests.get('https://sinoptik.com.ru/погода-москва') # сперва мы получили в переменную s код веб страницы в виде HTML
b=bs4.BeautifulSoup(s.text, "html.parser")              # преобразовали этот код в объект для парсинга
p3=b.select('.temperature .p3')                         # Команда select возвращает список из всех найденных тегов
pogoda1=p3[0].getText()                                 # с заданным селектором
p4=b.select('.temperature .p4')
pogoda2=p4[0].getText()
p5=b.select('.temperature .p5')
pogoda3=p5[0].getText()
p6=b.select('.temperature .p6')
pogoda4=p6[0].getText()
print('Утром :' + pogoda1 + ' ' + pogoda2)
print('Днём :' + pogoda3 + ' ' + pogoda4)
p=b.select('.rSide .description')
pogoda=p[0].getText()
print(pogoda.strip())
print(s.status_code, s.encoding, s.headers["Content-Type"], s.cookies)
