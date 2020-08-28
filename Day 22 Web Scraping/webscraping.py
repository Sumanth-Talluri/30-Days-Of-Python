from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

tables = soup.find_all('table')

for table in tables:
    for td in table:
        try:
            print(td.text)
        except:
            continue
