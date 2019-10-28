import time

from bs4 import BeautifulSoup
import requests


visited = {}
queue = []


def fetch(url):
    return requests.get(url)


def get_links(soup):
    return soup.find_all('a')


def enqueue_link(url):
    pass


def crawl(url):
    print(f'Fetching {url}...')
    resp = fetch(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        links = get_links(soup)

        for link in links:
            href = link.get('href')
            if href.startswith('https://news.naver.com/main/read.nhn') and href not in visited:
                queue.append(href)
                visited[href] = 0
    else:
        print(f'Failed to fetch {url}')


if __name__ == '__main__':
    queue.append('https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=293&aid=0000025345&date=20191016&type=1&rankingSeq=9&rankingSectionId=105')

    while queue:
        url = queue.pop()
        crawl(url)
        time.sleep(1)