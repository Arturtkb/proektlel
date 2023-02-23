import requests

from bs4 import BeautifulSoup
responce = requests.get("https://coinmarketcap.com")
if responce.status_code == 200:
    soup = BeautifulSoup(responce.text, features="html.parser")
    soup_text = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
    print(soup_text)
