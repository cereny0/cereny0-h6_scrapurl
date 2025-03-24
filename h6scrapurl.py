
import requests
from bs4 import BeautifulSoup

def gunluk_haber_link_olusturucu(sayfa_url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    r=requests.get(sayfa_url, headers=headers)
    soup = BeautifulSoup(r.content,'html.parser')
    liste = soup.find_all("div",{"class":"f-cat f-item"})
    for i in liste:
        print("===================================")
        for b in i.findAll("ul", {"class":"list underline"}):
        #print(b)
            for link in b.findAll('a'):
                 my_link = link.get('href') + "\n"
                 newlink = f"https://www.milligazete.com.tr{my_link}"
                 print(newlink)
                 with open('ist.txt', 'a', encoding="utf-8") as file:
                  file.write(newlink + "\n")
listem = [
    'https://www.milligazete.com.tr/arsiv/2025-03-22',
    'https://www.milligazete.com.tr/arsiv/2025-03-23',
    'https://www.milligazete.com.tr/arsiv/2025-03-24',
    'https://www.milligazete.com.tr/arsiv/2025-03-25',
    'https://www.milligazete.com.tr/arsiv/2025-03-26'
]
for gunlink in listem:
    gunluk_haber_link_olusturucu(gunlink)



