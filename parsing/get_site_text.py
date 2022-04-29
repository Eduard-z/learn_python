import requests
import html2text
import bs4
s=requests.get('https://24score.pro/')
d = html2text.HTML2Text().handle(s.text)
print(d, file = open("qqq.txt", "w", encoding="utf-8"))
