#!/usr/bin/python
#-*-coding:utf-8-*-

import requests
import time

#串行执行版本
def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all(sites):
    for site in sites:
        download_one(site)


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