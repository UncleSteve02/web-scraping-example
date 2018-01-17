import requests
from bs4 import BeautifulSoup
page = requests.get("http://www.espn.com/nba/team/schedule/_/name/phi/").text

soup = BeautifulSoup(page, 'html.parser')
trs = soup.find_all('tr')
for tr in trs:
    if "evenrow" not in tr['class'] and "oddrow" not in tr['class']:
        continue
    
    tds = tr.find_all('td')
    print(tds[0].text)
    print(tds[1].text)
    print(tds[2].text)
    print
