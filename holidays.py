import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.checkiday.com", verify=False).text

soup = BeautifulSoup(page, 'html.parser')
h2s = soup.find_all('h2')
for h2 in h2s:
    if h2.a['href'].startswith("https://www.checkiday.com"):
        print(h2.a.string)

file = open("events", "w")
file.write("<html>\n")
file.write(" <head>\n")
for h2 in h2s:
    if h2.a['href'].startswith("https://www.checkiday.com"):
        file.write(str(h2.a) + "\n")
file.write(" </head>\n")
file.write("</html>\n")
file.close()
