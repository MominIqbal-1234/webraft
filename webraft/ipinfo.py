import json
from requests import get
from functools import lru_cache



def publicip():
    ipdata = get(f'https://api.ipify.org?format=json').text
    return json.loads(ipdata)


def UserIPData(self,request):
    ip =  request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
    if str(ip) == '127.0.0.1':
        raise RuntimeError(f"{ip} Not Vaild")
    self.ipdata = get(f'http://ip-api.com/json/{ip}?fields=66846719').text
    return json.loads(self.ipdata)
        