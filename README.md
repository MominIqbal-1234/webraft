# WebRaft

creating and reading JSON Web Tokens, extracting user agent
information, retrieving IP data, and creating and reading API keys

# install webraft
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
request is an object that represents an incoming HTTP request <br> webraft take every function request object <br>
this doc show use to request in different python web framework

```
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
from webraft.core import JWTToken

token = JWTToken(secret_key='my_key',expiry_token=1,framework='django',algorithm='HS256')


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
token1 = token.read(request,"username","user_id")

```

![Screenshot (29)](https://github.com/MominIqbal-1234/jwt_django/assets/61788052/b829f7d0-4197-40ae-a771-3eae7dbd9c38)



## Add Custome Header

```python
 token1 = token.read(request,'username','user_id',header="myheader")

```
![Screenshot (31)](https://github.com/MominIqbal-1234/jwt_django/assets/61788052/932c4295-6431-4d96-8e66-06ee14b8ac10)


## Authenticated Token

This function returns a boolean value indicating whether the user is authenticated or not

```
print(token.is_authenticated()) # return bool
```


## User Device Info

The MetaData class extracts user agent information from a request and
provides methods to retrieve device, OS, browser, and other related information

```python

from webraft.core import MetaData

os_is = MetaData(request,'fastapi').os_is(),
browser_is = MetaData(request,'fastapi').browser_is(),
deviceIs = MetaData(request,'fastapi').deviceIs(),
mobileIs = MetaData(request,'fastapi').mobileIs(),
tabletIs = MetaData(request,'fastapi').tabletIs(),
touchCapableIs = MetaData(request,'fastapi').touchCapableIs(),

```
![Screenshot (33)](https://github.com/MominIqbal-1234/jwt_django/assets/61788052/902d85ad-389f-4115-a219-a1cb2a8f2642)


## IP Info
The IPinfo class returns user IP data
```python
from webraft.core import IPinfo
print(IPinfo(request).get())
```




## Create API-keys
The APIKey class provides for creating, reading, retrieving data from API keys.
```python
from webraft.core import APIKey

api_key = APIKey("my_key").create({
        "trail_key":"True",
    })
```

## Read API-Key
This function read the api key and return the list or dict.
```python
from webraft.core import APIKey

token1 = APIKey("my_key").read("myapikey","trail_key")
```






<br>
https://github.com/MominIqbal-1234/webraft



Check Our Site : https://mefiz.com/about </br>
Developed by : Momin Iqbal




