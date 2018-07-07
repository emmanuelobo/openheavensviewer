from bs4 import BeautifulSoup
import requests

def scrape_content():
	response = requests.get('https://www.openheavensdaily.com')
	html = response.content
	soup = BeautifulSoup(html, 'html.parser')
	print(soup.find_all('h2', {'class', 'date-header'})[0])

if __name__ == '__main__':
	scrape_content()