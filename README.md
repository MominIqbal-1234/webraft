### Downloads webraft
[![Downloads](https://static.pepy.tech/badge/webraft)](https://pepy.tech/project/webraft)



# WebRaft

creating and reading JSON Web Tokens, extracting user agent
information, retrieving IP data, and creating and reading API keys

# install webraft

link: https://pypi.org/project/webraft/

```python
pip install webraft
```

# Support

WebRaft Support Four Python web-framework

```
1) Django # django
2) Flask  # flask
3) FastAPI # fastapi
4) Bottle  # bottle
```

# Django Rest-API

## Create Secret Key

```python
from webraft.core import GenerateKey
print(GenerateKey.generate_key())
```

## Support Algorithm

```
HS256
HS512
HS384
```

## request

request is an object that represents an incoming HTTP request `<br>` webraft take every function request object `<br>`
this doc show use to request in different python web framework

```python
# Django
def home(request):
  pass

# FastAPI
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def read_user(request: Request):
  pass

# Flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  request = request
  pass

# Bottle
from bottle import Bottle, request

app = Bottle()

@app.route('/')
def home():
    request = request
    pass


```

## Create Token

This function creates a token using the provided data and request.

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from webraft.core import JWTToken,generator,MetaData,APIKey

token = JWTToken(
      secret_key='my_key',
      expiry_token=120,
      framework='flask',
      algorithm='HS256'
      )


@api_view(['GET'])
def create_jwt_token(request):
  token1 = token.create(request,{
        "username":"admin",
        "user_id":1
    })
  return Response({"token1":token1})
```

## Read Token

read function pass the request and parameter and return json

```python
# Return all josn vlaues
token1 = token.read(request)

# Return specific json 
token1 = token.getToken(request,'authorization')

```



## Check Expiry Token

```python
 token1 = token.checkExpiry(token.getToken(request,'authorization'))

```



## User Device Info

The MetaData class extracts user agent information from a request and
provides methods to retrieve device, OS, browser, and other related information

```python

from webraft.core import MetaData

os_is = MetaData(request,'fastapi').os_is,
browser_is = MetaData(request,'fastapi').browser_is,
deviceIs = MetaData(request,'fastapi').deviceIs,
mobileIs = MetaData(request,'fastapi').mobileIs,
tabletIs = MetaData(request,'fastapi').tabletIs,
touchCapableIs = MetaData(request,'fastapi').touchCapableIs,

```


## IP Info

The IPinfo class returns user IP data

```python
from webraft.core import IPinfo
print(IPinfo().get(request))
```

## Create API-keys

The APIKey class provides for creating, reading, retrieving data from API keys.

```python

key = APIKey(api_secret_key='my_key',algorithm='HS256')
    token1 = key.create({"username":"momin","userid":1})
    readToken =key.read(token1)
```





https://github.com/MominIqbal-1234/webraft

Check Our Site : https://mefiz.com/about

Developed by : Momin Iqbal

