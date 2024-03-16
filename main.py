from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_links(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(req).read()
    soup = BeautifulSoup(html_page, 'html.parser')
    soup.body.get_text(' ', strip=True)
    links = []
    for link in soup.select('a[href^="https://"]'):
        links.append(link['href'])
    return links

def get_content(url):
    return url



print(get_links('https://stackoverflow.com/questions/53911695/scrape-urls-using-beautifulsoup-in-python-3'))