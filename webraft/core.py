import jwt
import datetime
from cryptography.fernet import Fernet
from .ipinfo import IPInfo
from functools import lru_cache
from requests import get
import json
from user_agents import parse
try:
    from django.middleware import csrf
    from django_user_agents.utils import get_user_agent
except:
    pass


__name__ = "webraft"
__verion__ = "1.0"

"""


This project developed by Momin Iqbal
Support : mefiz.com
================================================================================================================

WebRaft Support Four Python web-framework 
1) Django
2) Flask
3) FastAPI
4) Bottle

Feuture:
The code defines several classes for creating and reading JSON Web Tokens, extracting user agent
information, retrieving IP data, and creating and reading API keys.
----------------------------------------------------------------------------------------------------------------

Check Our Site : https://mefiz.com


"""


_framework = [
"django",
"flask",
"fastapi",
"bottle",
]



# HS256
# HS512
# RS256
# 


class JWTToken:
    def __init__(self, secret_key=None,expiry_token=None,framework=None):
        """
        The JWTToken class that creates and reads JSON Web Tokens
        with a specified secret key, expiry date, and framework.
        
        """
        self.validateexpirytoken(expiry_token)
        self.validateframework(framework)
        self.secret_key = secret_key
        self.expiry_token = int(expiry_token)
        self.framework=framework
        self.today = datetime.datetime.now()
        self.algorithm = "HS512"
        
        
    def create(self,request,data) -> str:
        """
        This function creates a token using the provided data and request.
        
        :param request: The request object
        :param data: The `data` parameter is a variable
        """
        self.data = data
        self.request = request
        return ProcessToken._create_token(self,self.request)



    def read(self, request, *args,header=None) -> list or dict:
        """
        This read function using the provided data and request.
        
        :param request: The HTTP request object
        :param header: The header parameter is an optional argument that specifies the name of the
        header that contains the authentication token. If this parameter is not provided, the default
        header name 'authorization' will be used
        :return: a list or a dictionary.
        """
        self.request = request
        self.args = args
        self.header = header
        if header == None:
            self.header = 'authorization'

        if self.is_authenticated() == False:
            return {"invaild-token": "token expire"}
        try:
            return ProcessToken.get_data(self)
        except KeyError as e:
            raise KeyError(f"invalid key {e}")

    def is_authenticated(self) -> bool:
        """
        This function returns a boolean value indicating whether the user is authenticated or not.
        :return: A boolean value is being returned
        """
       
        return ProcessToken.anonymous(self)
        
    def validateframework(self,framework):
        if framework == None:
            raise ValueError("framework not define")
        elif framework not in _framework:
            raise ValueError(f"framework support",_framework)
    def validateexpirytoken(self,expiry_token):
        if expiry_token == None:
            raise ValueError("add token expire date")
        elif expiry_token <= 0:
            raise ValueError("0 expiry_token not valid")


class ProcessToken(JWTToken):
    def _create_token(self,request):
        return Json.encode(self,request)
    
    def get_data(self):
        try:
            if self.framework == 'fastapi' or 'flask' or 'bottle':
                # return ProcessToken.datalist(self,self.request.headers.get('authorization'))
                return ProcessToken.datalist(self,self.request.headers.get((self.header)))
            elif self.framework == 'django':  
                return ProcessToken.datalist(self,self.request.headers[(self.header)])
           
        except ValueError:
            raise ValueError("authorization header not exist")

    # def expiryInfo(self):
    def token_date(self):
        try:
            if self.framework == 'fastapi' or 'flask' or 'bottle':
                return Json.decode(self, self.request.headers.get((self.header)))
            elif self.framework == 'django':  
                return Json.decode(self, self.request.headers[(self.header)])
        except ValueError:
            raise ValueError("authorization header not exist")

    def validate(self):
        self.date = ProcessToken.token_date(self)
        self.expirydate = self.date.get("expiry_date")
        self.todaydate = str(self.today)[2:]

        self.expirydate = str(self.expirydate)[:8]
        self.todaydate = str(self.todaydate)[:8]

        self._expirydate = datetime.datetime.strptime(
            f"{self.expirydate}", "%y-%m-%d")
        self._todaydate = datetime.datetime.strptime(
            f"{self.todaydate}", "%y-%m-%d")
        if self._expirydate > self._todaydate:
            return True
        elif self._expirydate < self._todaydate:
            return False
        else:
            return True

    def anonymous(self):
        return ProcessToken.validate(self)

    def datalist(self, token):
        if len(self.args) != 0:
            self.DataList = []
            self.values = Json.decode(self, token)
            for i in self.args:
                self.DataList.append(self.values.get(i))
            return self.DataList
        else:
            return Json.decode(self, token)
    


class Json:
    def dublication(self):
        self.check = list(self.data)
        self.value = [(i) for i in self.check if "expiry_date" == i]

        if self.value == []:
            return True
        if self.value[0] == "expiry_date":
            raise ValueError("expiry_date already exist")

    def encode(self,request):
        Json.dublication(self)
        self.expire_date = self.today + datetime.timedelta(days=self.expiry_token)
        if self.framework == 'django':
            self.data.update({
                "expiry_date": str(self.expire_date)[2:],
                "X-CSRFToken":csrf.get_token(request)
            })
        else:
            self.data.update({
                "expiry_date": str(self.expire_date)[2:]
            })
        try:
            return jwt.encode(self.data, self.secret_key, algorithm=self.algorithm)
        except Exception as e:
            raise ValueError(e)

    def decode(self, token):
        try:
            return jwt.decode(token, self.secret_key, algorithms=self.algorithm)
        except Exception as e:
            raise ValueError(e)





class GenerateKey:
    """
    The GenerateKey class contains a method to generate a Fernet key.
    """
    def generate_key():
        return Fernet.generate_key()



class MetaData:
    def __init__(self,request,framework=None):
        
        """
        The MetaData class extracts user agent information from a request and
        provides methods to retrieve device, OS, browser, and other related information.
        """
        self.framework = framework
        self.validateframework()
        if framework == 'fastapi' or framework =='flask' or framework =='bottle':
            self.user_agent_string = request.headers.get('User-Agent')
            self.user_agent = parse(self.user_agent_string)
        else:
            self.user_agent = get_user_agent(request)
  

    def device_is(self) -> str: return self.user_agent.device.family
    """
    This function returns the device family of a user agent.
    :return: The function `device_is` is returning user device
    user agent.
    """
        
    def os_is(self) -> str:return self.user_agent.os.family
    """
    This function returns the operating system family of the user agent.
    :return: user operating system
    """
        
        
    def browser_is(self) -> str:return self.user_agent.browser.family
    """
    This function returns the browser family of the user agent.
    :return: a string that represents the browser family of the user agent.
    """
      

    def deviceIs(self) -> str:return self.user_agent.get_device()
    
        
    def osIs(self) -> str:return self.user_agent.get_os()
        
    def browserIs(self) -> str:return self.user_agent.get_browser()
       
    def mobileIs(self) -> bool:return self.user_agent.is_mobile
        
    def tabletIs(self) -> bool:return self.user_agent.is_tablet
      
    def touchCapableIs(self) -> bool:return self.user_agent.is_touch_capable
        
    def pcIs(self) -> bool:return self.user_agent.is_pc
        
    def botIs(self) -> bool:return self.user_agent.is_bot
        
    def emailClientIs(self) -> bool: return self.user_agent.is_email_client

    
    def validateframework(self):
        if self.framework == None:
            raise ValueError("framework not define")
        elif self.framework not in _framework:
            raise ValueError(f"framework support",_framework)
       

class IPinfo:
    """
    The IPinfo class returns user IP data
    """
    def get(self,request):
        return IPInfo().UserIPData(request)
        




class APIKey:
    """
    The APIKey class provides for creating, reading, retrieving data from API keys.
    """
    def __init__(self, api_secret_key=None):
        self.api_secret_key = api_secret_key
        self.today = datetime.datetime.now()

    def create(self,data) -> str:
        """
        This function creates an API key using the provided data.
        
        :param data: The data parameter is the input data that will be used to create an API key. It could
        be any relevant information such as application details, or any other required information.
        """
        self.data = data
        return self._create_apikey()

    def read(self,apikey,*args) -> list or dict:
        """
        This function read the api key and return the list or dict.
        """
        self.apikey = apikey
        self.args = args
        return self.apikey_data()

    def dublication(self):
        self.check = list(self.data)
        self.value = [(i) for i in self.check if "created_date" == i]

        if self.value == []:
            return True
        if self.value[0] == "created_date":
            raise ValueError("created_date already exist")



    def encode(self):
        self.dublication()
        self.today = datetime.datetime.now()
        self.data.update({
                "created_date": str(self.today),
            })
        try:
            return jwt.encode(self.data, self.api_secret_key, algorithm="HS512")
        except Exception as e:
            raise ValueError(e)

    def decode(self):
        try:
            return jwt.decode(self.apikey, self.api_secret_key, algorithms="HS512")
        except Exception as e:
            raise ValueError(e)

    def data_list(self):
        if len(self.args) != 0:
            self.dataList = []
            self.values = self.decode()
            for i in self.args:
                self.dataList.append(self.values.get(i))
                return self.dataList
        else:
            return self.decode()
        
    def _create_apikey(self):
        return self.encode()

    def apikey_data(self):
        return self.data_list()



 
  

    