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

def get_text(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(req).read()
    soup = BeautifulSoup(html_page, 'html.parser')
    return soup.get_text(separator='\r', strip=True)

def scrape(url, current_depth, maximum_depth, link_index=0):

    print(f"[{current_depth}][{link_index}]")
    f = open(f"files/[{current_depth}][{link_index}].txt", "w", encoding="utf-8")
    text = get_text(url)
    f.write(text)
    f.close()

    if current_depth == maximum_depth:
        return

    links = get_links(url)
    for link_index, link in enumerate(links):
        scrape(link, current_depth + 1, maximum_depth, link_index)


scrape('https://stackoverflow.com/questions/53911695/scrape-urls-using-beautifulsoup-in-python-3', 0, 1)
