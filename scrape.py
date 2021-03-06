import bs4 as bs
import urllib.request


def peps():
    """
    scrapes all urls with the pep prefix from the pep index page and returns them as a set
    note: scraped peps look like this - /dev/peps/pep-0010/ - and are strings.
    :return:
    """
    sauce = urllib.request.urlopen('https://www.python.org/dev/peps/').read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    peps = [url.get('href') for url in soup.find_all('a') if "/dev/peps/pep-" in url.get('href')]
    return peps


def title(push_pep):
    """
    gets full title of pep from the page of the pep
    :param push_pep:
    :return:
    """
    sauce = urllib.request.urlopen(push_pep).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    return soup.find(class_='page-title').text

