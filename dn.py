import requests
import json as js
import socks
import socket
import urllib.request
from instagrapi import Client
from instagrapi.exceptions import ClientConnectionError
from time import sleep
from selenium import webdriver


def getProxy(ip, port):
    proxies = {
    "socks5": f"http://{ip}:{port}",
    "socks5": f"https://{ip}:{port}"
    }
    return proxies

def proxyControls(ip, port):
    proxies = getProxy(ip, port)
    try:
        response = requests.get("https://google.com", proxies=proxies, timeout=20)
    except OSError as e:
        print("Proxy calismadi", e)
        return False
    else:
        print(response.elapsed.total_seconds())
        return True
        



def instaConnection(ip, port):
    try:
        cl = Client()
        cl.set_proxy(f'https://{ip}:{port}')
        cl.login('elda.r2372', 'ramiz123')
    except ClientConnectionError as e:
        print(e)
    else:
        print("OK", ip, port, sep=':')
        return cl


def getProxyList():
    proxy_list = []
    port_list = []
    headers = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    res = requests.get("https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=socks5", headers=headers)
    data = res.text
    jdata = js.loads(data)['data']
    for proxy in jdata:
        proxy_list.append(proxy['ip'])
        port_list.append(proxy['port'])
    return proxy_list, port_list

ip_list, port_list = getProxyList()
for ip, port in zip(ip_list, port_list):
    if(proxyControls(ip, port)):
        print(ip, port)
        # instaConnection(ip, port)
    else:
        pass

# print(proxyControls('158.69.197.113','7497'))

# user_id = int(cl.user_id_from_username("illegalism666"))
# medias = cl.user_medias(user_id, 20)
# print(medias)