import bs4 as bs
import urllib.request

def get_PEP_set():
    sauce = urllib.request.urlopen('https://www.python.org/dev/peps/').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    peps = {url.get('href') for url in soup.find_all('a') if "/dev/peps/pep-" in url.get('href')}

    # print(peps)
    return peps
