from bs4 import BeautifulSoup
import requests
url = 'https://www.scrapethissite.com/pages/forms/'
page=requests.get(url)
#print(requests.get(url))
soup=BeautifulSoup(page.text,'html.parser')
#print(soup)
soup.find('div')
print(soup.find('th').text.strip())
