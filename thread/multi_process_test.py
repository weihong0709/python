import concurrent.futures
import requests
import threading
import time


def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all(sites):
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(download_one, sites)


def main():
    sites = [
        'http://mil.news.sina.com.cn/',
        'http://news.sina.com.cn/world/',
        'http://sports.sina.com.cn/nba/',
        'http://sports.sina.com.cn/g/premierleague/'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()