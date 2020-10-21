# -*- coding: utf-8 -*-
import pandas as pd
data = pd.read_csv('csv')

from urllib.parse import urlparse

urls, domains = [], []
for url in data.urls:
    if type(url) == str and 'https' in url:
        urls.append(url)
        domains.append(urlparse(url).netloc)

domains = set(domains)

import json
import requests

def get_json(domain):
    response = requests.get('http://api.whois.vu/?q='+domain)
    bytes_data = response.content
    json_data = bytes_data.decode('utf8')
    data = json.loads(json_data)
    return data

def get_free(domains):

    free = []
    f = open('free_domains.txt', 'w')
    for domain in domains:
        data = get_json(domain)
        if data['available'] == 'yes':
            free.append(data['domain'])
            f.write(data['domain']+'\n')
        if len(free)==20:
            f.close()
            return free

print(get_free(domains))

