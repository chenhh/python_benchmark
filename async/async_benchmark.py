# -*- coding: UTF-8 -*-
import requests
import time


def sequential_request():
    url = 'https://www.google.com.tw/'
    start_time = time.time()
    for i in range(10):
        send_req(url)


def send_req(start_time, url):
    t = time.time()
    print(f"Send a request at {t-start_time} seconds.")
    res = requests.get(url)
    t = time.time()
    print(f"Receive a response at {t-start_time} seconds.")

