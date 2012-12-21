import os
import urllib2
from bs4 import BeautifulSoup

host_url = 'http://www.computer.org'
base_url = host_url + '/csdl/proceedings'

def get_conference_page_url(conference):
    return "/".join([base_url, conference, 'index.html'])

def get_conference_page_url_by_year(conference, year):
    url = "/".join([base_url, conference, str(year), 'index.html'])
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    for link in soup.find_all('a', class_='remote'):
        return host_url + link['href']

def open_url(url):
    os.system('open %s' %(url))
